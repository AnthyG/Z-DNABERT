from typing import Iterable
from src.prediction_result import PredictionResult

class PredictionResultFormatter:
    def file_name_common(self, prediction_result: PredictionResult, now_time_as_string_for_file_name: str) -> str:
        raise NotImplementedError()

    def file_name_variation(self, prediction_result: PredictionResult, now_time_as_string_for_file_name: str) -> str:
        raise NotImplementedError()

    def format(self, prediction_result: PredictionResult) -> Iterable[str]:
        raise NotImplementedError()
