import logging
from tqdm.auto import tqdm
import torch
import scipy
from transformers import BertTokenizer, BertForTokenClassification, PreTrainedModel
from src.sequence_helper import SequenceHelper

class ZdnabertModel:
    logger: logging.Logger
    using_cuda: bool
    tokenizer: BertTokenizer
    model: PreTrainedModel
    
    def __init__(
        self,
        data_path: str,
        model_name: str,
        model_confidence_threshold: float,
        minimum_sequence_length: int,
        use_cuda: bool,
    ):
        self.logger = logging.getLogger(__name__)
        self.sequence_helper = SequenceHelper()
        
        self.data_path = data_path
        self.model_name = model_name
        self.model_confidence_threshold = model_confidence_threshold
        self.minimum_sequence_length = minimum_sequence_length
        self.use_cuda = use_cuda

    def load(self) -> None:
        self.prepare_bert_model()
        self.check_cuda()
        self.prepare_cuda()

    def prepare_bert_model(self) -> None:
        self.tokenizer = BertTokenizer.from_pretrained(self.data_path)
        self.model = BertForTokenClassification.from_pretrained(self.data_path)

    def check_cuda(self) -> None:
        if self.use_cuda:
            self.using_cuda = torch.cuda.is_available()
            if not self.using_cuda:
                raise RuntimeError('cuda is set to be used but not available')
        else:
            self.using_cuda = False
    
    def prepare_cuda(self) -> None:
        if self.using_cuda:
            self.model.cuda()
        else:
            self.model.cpu()

    def kmer_and_split_seq(self, seq: str) -> list:
        kmer_seq = self.sequence_helper.seq2kmer(seq, 6)
        seq_pieces = self.sequence_helper.split_seq(kmer_seq)
        return seq_pieces

    def run_prediction(
        self,
        seq_pieces: list,
        progress_bar = tqdm,
    ) -> list:
        preds = []
        with torch.no_grad():
            for seq_piece in progress_bar(seq_pieces, 'prediction on sequence pieces'):
                input_ids = torch.LongTensor(self.tokenizer.encode(' '.join(seq_piece), add_special_tokens=False))
                input_ids_unsqueezed = None
                if self.using_cuda:
                    input_ids_unsqueezed = input_ids.cuda().unsqueeze(0)
                else:
                    input_ids_unsqueezed = input_ids.cpu().unsqueeze(0)
                outputs = torch.softmax(self.model(input_ids_unsqueezed)[-1], axis = -1)[0,:,1]
                preds.append(outputs.cpu().numpy())
        return preds

    def stitch_preds(
        self,
        preds: list,
        progress_bar = tqdm,
    ):
        return self.sequence_helper.stitch_np_preds(preds, progress_bar)
    
    def label_stitched_preds(self, stitched_preds):
        labeled, max_label = scipy.ndimage.label(stitched_preds>self.model_confidence_threshold)
        return labeled, max_label