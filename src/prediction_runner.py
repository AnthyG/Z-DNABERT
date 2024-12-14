from Bio import SeqIO
from src.prediction_input import PredictionInput
from src.prediction_input_file import PredictionInputFile
from src.prediction_result import PredictionResult
from src.zdnabert_model import ZdnabertModel
from src.sequence_variation import SequenceVariation

class PredictionRunner:
    def run(
        self,
        prediction_inputs: list[PredictionInput]
    ) -> list[PredictionResult]:
        prediction_results = []
        for prediction_input in prediction_inputs:
            new_prediction_results = self.run_on_prediction_input(prediction_input)
            prediction_results.extend(new_prediction_results)
        return prediction_results

    def run_on_prediction_input(
        self,
        prediction_input: PredictionInput
    ) -> list[PredictionResult]:
        prediction_results = []
        model = prediction_input.get_model()
        prediction_input_files = prediction_input.get_files()
        sequence_variations = prediction_input.get_sequence_variations()
        for prediction_input_file in prediction_input_files:
            new_prediction_results = self.run_on_prediction_input_file(model, prediction_input_file, sequence_variations)
            prediction_results.extend(new_prediction_results)
        return prediction_results

    def run_on_prediction_input_file(
        self,
        model: ZdnabertModel,
        prediction_input_file: PredictionInputFile,
        sequence_variations: list[SequenceVariation],
    ) -> list[PredictionResult]:
        prediction_results = []
        file_handle = prediction_input_file.open()
        for seq_record in SeqIO.parse(file_handle, 'fasta'):
            seq = str(seq_record.seq)
            new_prediction_results = self.run_on_prediction_input_seq_variations(
                model,
                seq,
                sequence_variations,
            )
            prediction_results.extend(new_prediction_results)
        prediction_input_file.close()
        return prediction_results
    
    def run_on_prediction_input_seq_variations(
        self,
        model: ZdnabertModel,
        seq: str,
        sequence_variations: list[SequenceVariation],
    ) -> list[PredictionResult]:
        prediction_results = []
        for sequence_variation in sequence_variations:
            new_prediction_result = self.run_on_prediction_input_seq_variation(
                model,
                seq,
                sequence_variation,
            )
            prediction_results.append(new_prediction_result)
        return prediction_results
    
    def run_on_prediction_input_seq_variation(
        self,
        model: ZdnabertModel,
        input_seq: str,
        sequence_variation: SequenceVariation,
    ) -> PredictionResult:
        seq = sequence_variation.create_variation(input_seq)
        seq_len = len(seq)
        model.load()
        seq_pieces = model.kmer_and_split_seq(seq)
        preds = model.run_prediction(seq_pieces)
        stitched_preds = model.stitch_preds(preds)
        labeled, max_label = model.label_stitched_preds(stitched_preds)
        return PredictionResult(
            '{}'.format(sequence_variation.get_title()),
            sequence_variation,
            model.minimum_sequence_length,
            seq_len,
            labeled,
            max_label,
        )
        