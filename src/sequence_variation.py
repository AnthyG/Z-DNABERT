class SequenceVariation:
    def get_title(self) -> str:
        raise NotImplementedError()
    
    def create_variation(self, seq: str) -> str:
        raise NotImplementedError()

    def derive_candidate_start_and_end(self, seq_len: int, candidate: list[int]) -> (int, int):
        raise NotImplementedError()
