from typing import Iterable

from Bio import SeqIO
from tqdm.auto import tqdm

from src.prediction_input import PredictionInput
from src.prediction_result import PredictionResult
from src.sequence_variation import SequenceVariation
from src.zdnabert_model import ZdnabertModel


class PredictionRunner:
    def run(
        self,
        prediction_inputs: list[PredictionInput],
        progress_bar = tqdm,
    ) -> Iterable[PredictionResult]:
        for prediction_input in progress_bar(prediction_inputs, 'inputs'):
            model = prediction_input.get_model()
            prediction_input_files = prediction_input.get_files()
            sequence_variations = prediction_input.get_sequence_variations()
            for prediction_input_file in progress_bar(prediction_input_files, 'files'):
                file_name = prediction_input_file.file_name
                file_handle = prediction_input_file.open()
                for seq_record in progress_bar(SeqIO.parse(file_handle, 'fasta'), 'records'):
                    seq = str(seq_record.seq)
                    seq_record_name = seq_record.name
                    for sequence_variation in progress_bar(sequence_variations, 'sequences'):
                        yield self.run_on_prediction_input_seq_variation(
                            model,
                            seq,
                            sequence_variation,
                            file_name,
                            seq_record_name,
                            progress_bar,
                        )
                prediction_input_file.close()
    
    def run_on_prediction_input_seq_variation(
        self,
        model: ZdnabertModel,
        input_seq: str,
        sequence_variation: SequenceVariation,
        file_name: str,
        seq_record_name: str,
        progress_bar = tqdm,
    ) -> PredictionResult:
        seq = sequence_variation.create_variation(input_seq)
        seq_len = len(seq)

        model.load()
        seq_pieces = model.kmer_and_split_seq(seq)
        preds = model.run_prediction(seq_pieces, progress_bar)
        stitched_preds = model.stitch_preds(preds, progress_bar)
        labeled, max_label = model.label_stitched_preds(stitched_preds)
        
        return PredictionResult(
            model.model_name,
            model.model_confidence_threshold,
            model.minimum_sequence_length,
            file_name,
            seq_record_name,
            sequence_variation,
            seq_len,
            labeled,
            max_label,
        )
        