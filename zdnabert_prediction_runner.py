import os
import logging
from src.prediction_runner import PredictionRunner
from src.prediction_input import PredictionInput
from src.prediction_input_file_from_filesystem import PredictionInputFileFromFilesystem
from src.zdnabert_model import ZdnabertModel
from src.sequence_variation_normal import SequenceVariationNormal
from src.sequence_variation_reverse_complement import SequenceVariationReverseComplement
from src.prediction_result_formatter_bed_file import PredictionResultFormatterBedFile
from src.zdnabert_model_downloader import ZdnabertModelDownloader

class ZdnabertPredictionRunner:
    def __init__(self):
        logging.basicConfig(
            filename='example.log',
            encoding='utf-8',
            format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
            level=logging.DEBUG
        )
        
        self.logger = logging.getLogger(__name__)
    
    def run(
        self,
        model_download_path: str,
        output_path: str,
    ) -> None:
        zdnabert_model_downloader = ZdnabertModelDownloader()
        zdnabert_model_downloader.download_models(model_download_path)
        zdnabert_model_downloader.download_metas(model_download_path)
        
        zdnabert_model_mm_kouzine_mct025_msl12_true = ZdnabertModel(
            os.path.join(model_download_path, 'MM_kouzine'),
            model_name='MM_kouzine',
            model_confidence_threshold=0.25,
            minimum_sequence_length=12,
            use_cuda_if_available=True,
        )
    
        prediction_input_file_1 = PredictionInputFileFromFilesystem(
            'humantshz2promoterexon1_test.fa',
            os.path.join('.', 'input', 'humantshz2promoterexon1_test.fa'),
        )
    
        sequence_variation_normal = SequenceVariationNormal()
        sequence_variation_reverse_complement = SequenceVariationReverseComplement()
        
        prediction_input_1 = PredictionInput(
            zdnabert_model_mm_kouzine_mct025_msl12_true,
            [
                prediction_input_file_1,
            ],
            [
                sequence_variation_normal,
                sequence_variation_reverse_complement,
            ],
        )
        
        prediction_inputs = [
            prediction_input_1,
        ]
    
        prediction_result_formatter_bed_file = PredictionResultFormatterBedFile()
        
        prediction_runner = PredictionRunner()
        
        for prediction_result in prediction_runner.run(prediction_inputs):
            bed_file_name_seq = prediction_result_formatter_bed_file.file_name(prediction_result)
            
            #print(bed_file_name_seq)
            #print(bed_file_name)
    
            bed_file_seq_handler = open(os.path.join(output_path, bed_file_name_seq), 'w')
            
            #print('track name="{name}" priority=1'.format(name=model_params_as_string))
            #print('track name="{name}" priority=2'.format(name=seq_name))
            for line in prediction_result_formatter_bed_file.format(prediction_result):
                #print(line)
                bed_file_seq_handler.write("{}\n".format(line))
    
            bed_file_seq_handler.close()
            #print()


if __name__ == '__main__':
    zdnabert_prediction_runner = ZdnabertPredictionRunner()
    zdnabert_prediction_runner.run('./pytorch_models', './output')
