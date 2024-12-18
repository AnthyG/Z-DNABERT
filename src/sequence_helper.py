import numpy as np
from tqdm.auto import tqdm

class SequenceHelper:
    
    base_pair_opposite_map = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }

    def upper_seq(self, seq: str) -> str:
        return seq.upper()
    
    def complement_nucleobase(self, nucleobase: str) -> str:
        return self.base_pair_opposite_map[nucleobase] if nucleobase in self.base_pair_opposite_map else nucleobase
    
    def complement_seq(self, seq: str) -> str:
        return ''.join([self.complement_nucleobase(nucleobase) for nucleobase in seq])
    
    def reverse_seq(self, seq: str) -> str:
        return seq[::-1]
    
    def seq2kmer(self, seq: str, k: int):
        kmer = [seq[x:x+k] for x in range(len(seq)+1-k)]
        return kmer
    
    def split_seq(self, seq: str, length: int = 512, pad: int = 16):
        res = []
        for st in range(0, len(seq), length - pad):
            end = min(st+length, len(seq))
            res.append(seq[st:end])
        return res

    def stitch_np_preds(
        self,
        np_seqs,
        progress_bar=tqdm,
        pad=16,
    ):
        res = np.array([])
        for seq in progress_bar(np_seqs, 'stitching predictions'):
            res = res[:-pad]
            res = np.concatenate([res, seq])
        return res
