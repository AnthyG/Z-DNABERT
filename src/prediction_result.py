from src.sequence_variation import SequenceVariation

class PredictionResult:
    def __init__(
        self,
        title: str,
        sequence_variation: SequenceVariation,
        minimum_sequence_length: int,
        seq_len: int,
        labeled,
        max_label: int,
    ):
        self.title = title
        self.sequence_variation = sequence_variation
        self.minimum_sequence_length = minimum_sequence_length
        self.seq_len = seq_len
        self.labeled = labeled
        self.max_label = max_label
