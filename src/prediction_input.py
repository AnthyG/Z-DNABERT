from src.zdnabert_model import ZdnabertModel
from src.prediction_input_file import PredictionInputFile
from src.sequence_variation import SequenceVariation

class PredictionInput:
    def __init__(
        self,
        model: ZdnabertModel,
        files: list[PredictionInputFile],
        sequence_variations: list[SequenceVariation],
    ):
        self.model = model
        self.files = files
        self.sequence_variations = sequence_variations

    def get_model(self) -> ZdnabertModel:
        return self.model

    def get_files(self) -> list[PredictionInputFile]:
        return self.files

    def get_sequence_variations(self) -> list[SequenceVariation]:
        return self.sequence_variations
