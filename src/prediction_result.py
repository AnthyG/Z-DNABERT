from src.sequence_variation import SequenceVariation

class PredictionResult:
    def __init__(
        self,
        model_name: str,
        model_confidence_threshold: float,
        minimum_sequence_length: int,
        file_name: str,
        seq_record_name: str,
        sequence_variation: SequenceVariation,
        seq_len: int,
        labeled,
        max_label: int,
    ):
        self.model_name = model_name
        self.model_confidence_threshold = model_confidence_threshold
        self.minimum_sequence_length = minimum_sequence_length
        self.file_name = file_name
        self.seq_record_name = seq_record_name
        self.sequence_variation = sequence_variation
        self.seq_len = seq_len
        self.labeled = labeled
        self.max_label = max_label
    
    def get_model_params_as_string(self) -> str:
        return 'm={},mct={},msl={}'.format(self.model_name, self.model_confidence_threshold, self.minimum_sequence_length)
    
    def get_model_params_as_string_for_file_name(self) -> str:
        return 'm_{},mct_{},msl_{}'.format(self.model_name, self.model_confidence_threshold, self.minimum_sequence_length)
