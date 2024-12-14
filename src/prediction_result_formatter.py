from typing import Iterable
from src.prediction_result import PredictionResult

class PredictionResultFormatter:
    def format(self, prediction_result: PredictionResult) -> Iterable[str]:
        raise NotImplementedError()
