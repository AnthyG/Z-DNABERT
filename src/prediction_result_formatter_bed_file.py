from typing import Iterable
import numpy as np
from src.prediction_result_formatter import PredictionResultFormatter
from src.prediction_result import PredictionResult

class PredictionResultFormatterBedFile(PredictionResultFormatter):
    def file_name_common(self, prediction_result: PredictionResult, now_time_as_string_for_file_name: str) -> str:
        model_params_as_string_for_file_name = prediction_result.get_model_params_as_string_for_file_name()
        file_name = prediction_result.file_name
        seq_record_name = prediction_result.seq_record_name
        seq_record_key = '{}.{}.{}.{}'.format(file_name, seq_record_name, model_params_as_string_for_file_name, now_time_as_string_for_file_name)
        bed_file_name = '{}.bed'.format(seq_record_key)

        return bed_file_name
    
    def file_name_variation(self, prediction_result: PredictionResult, now_time_as_string_for_file_name: str) -> str:
        model_params_as_string_for_file_name = prediction_result.get_model_params_as_string_for_file_name()
        sequence_variation = prediction_result.sequence_variation
        file_name = prediction_result.file_name
        seq_record_name = prediction_result.seq_record_name
        seq_record_key = '{}.{}.{}.{}'.format(file_name, seq_record_name, model_params_as_string_for_file_name, now_time_as_string_for_file_name)
        seq_name = sequence_variation.get_title()
        seq_key = '{}.{}'.format(seq_record_key, seq_name)
        bed_file_name_seq = '{}.bed'.format(seq_key)

        return bed_file_name_seq
        
    def format(self, prediction_result: PredictionResult) -> Iterable[str]:
        sequence_variation = prediction_result.sequence_variation
        model_params_as_string = prediction_result.get_model_params_as_string()
        seq_name = sequence_variation.get_title()
        minimum_sequence_length = prediction_result.minimum_sequence_length
        seq_len = prediction_result.seq_len
        max_label = prediction_result.max_label
        labeled = prediction_result.labeled
        
        label_id = 1
        for label in range(1, max_label+1):
            candidate = np.where(labeled == label)[0]
            candidate_length = candidate.shape[0]
            if candidate_length>minimum_sequence_length:
                bed_name = '{},{},{}'.format(model_params_as_string, seq_name, label_id)
                
                candidate_start, candidate_end = sequence_variation.derive_candidate_start_and_end(seq_len, candidate)
                yield '0\t{start}\t{end}\t{name}'.format(start=candidate_start, end=candidate_end, name=bed_name)
                
                label_id += 1