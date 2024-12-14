from typing import Iterable
from src.prediction_result import PredictionResult

class PredictionResultFormatter:
    def file_name(self, prediction_result: PredictionResult) -> str:
        raise NotImplementedError()
    
    def format(self, prediction_result: PredictionResult) -> Iterable[str]:
        raise NotImplementedError()
