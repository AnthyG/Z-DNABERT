from src.sequence_variation import SequenceVariation
from src.sequence_helper import SequenceHelper

class SequenceVariationNormal(SequenceVariation):
    def __init__(self):
        self.sequence_helper = SequenceHelper()
    
    def get_title(self) -> str:
        return 'normal'
    
    def create_variation(self, seq: str) -> str:
        return self.sequence_helper.upper_seq(seq)

    def derive_candidate_start_and_end(self, seq_len: int, candidate: list[int]) -> (int, int):
        candidate_start = candidate[0]
        candidate_end = candidate[-1]
        return candidate_start, candidate_end
