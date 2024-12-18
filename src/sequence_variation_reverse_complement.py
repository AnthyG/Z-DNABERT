from src.sequence_variation import SequenceVariation
from src.sequence_helper import SequenceHelper

class SequenceVariationReverseComplement(SequenceVariation):
    def __init__(self):
        self.sequence_helper = SequenceHelper()
    
    def get_title(self) -> str:
        return 'rev-comp'
    
    def create_variation(self, seq: str) -> str:
        seq_uppered = self.sequence_helper.upper_seq(seq)
        seq_uppered_complemented = self.sequence_helper.complement_seq(seq_uppered)
        seq_uppered_complemented_reversed = self.sequence_helper.reverse_seq(seq_uppered_complemented)
        return seq_uppered_complemented_reversed

    def derive_candidate_start_and_end(self, seq_len: int, candidate: list[int]) -> (int, int):
        candidate_start = seq_len - candidate[-1]
        candidate_end = seq_len - candidate[0]
        return candidate_start, candidate_end
