from typing import Iterable
import numpy as np
from src.prediction_result_formatter import PredictionResultFormatter
from src.prediction_result import PredictionResult

class PredictionResultFormatterBedFile(PredictionResultFormatter):
    def format(self, prediction_result: PredictionResult) -> Iterable[str]:
        sequence_variation = prediction_result.sequence_variation
        minimum_sequence_length = prediction_result.minimum_sequence_length
        seq_len = prediction_result.seq_len
        max_label = prediction_result.max_label
        labeled = prediction_result.labeled
        
        label_id = 1
        for label in range(1, max_label+1):
            candidate = np.where(labeled == label)[0]
            candidate_length = candidate.shape[0]
            if candidate_length>minimum_sequence_length:
                
                
                # TODO
                model_params_as_string = 'lol'
                seq_name = 'wow'
                bed_name = '{},{},{}'.format(model_params_as_string, seq_name, label_id)


                
                candidate_start, candidate_end = sequence_variation.derive_candidate_start_and_end(seq_len, candidate)
                yield '0\t{start}\t{end}\t{name}'.format(start=candidate_start, end=candidate_end, name=bed_name)
                
                label_id += 1