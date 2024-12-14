import torch
from transformers import BertTokenizer, BertForTokenClassification, PreTrainedModel
import logging
from src.sequence_helper import SequenceHelper
import scipy

class ZdnabertModel:
    logger: logging.Logger
    is_cuda_available: bool
    tokenizer: BertTokenizer
    model: PreTrainedModel
    
    def __init__(
        self,
        data_path: str,
        model_name: str,
        model_confidence_threshold: float,
        minimum_sequence_length: int,
        use_cuda_if_available: bool,
    ):
        self.logger = logging.getLogger(__name__)
        self.sequence_helper = SequenceHelper()
        
        self.data_path = data_path
        self.model_name = model_name
        self.model_confidence_threshold = model_confidence_threshold
        self.minimum_sequence_length = minimum_sequence_length
        self.use_cuda_if_available = use_cuda_if_available

    def load(self) -> None:
        self.prepare_bert_model()
        self.check_cuda()
        self.prepare_cuda()

    def prepare_bert_model(self) -> None:
        self.tokenizer = BertTokenizer.from_pretrained(self.data_path)
        self.model = BertForTokenClassification.from_pretrained(self.data_path)

    def check_cuda(self) -> None:
        if self.use_cuda_if_available == True:
            self.is_cuda_available = torch.cuda.is_available()
            self.logger.info('cuda is {}'.format('available' if self.is_cuda_available else 'not available'))
        else:
            self.is_cuda_available = False
    
    def prepare_cuda(self) -> None:
        if self.is_cuda_available == True:
            self.model.cuda()
        else:
            self.model.cpu()

    def kmer_and_split_seq(self, seq: str) -> list:
        kmer_seq = self.sequence_helper.seq2kmer(seq, 6)
        seq_pieces = self.sequence_helper.split_seq(kmer_seq)
        return seq_pieces

    def run_prediction(self, seq_pieces: list) -> list:
        preds = []
        with torch.no_grad():
            for seq_piece in seq_pieces:
                input_ids = torch.LongTensor(self.tokenizer.encode(' '.join(seq_piece), add_special_tokens=False))
                input_ids_unsqueezed = None
                if self.is_cuda_available:
                    input_ids_unsqueezed = input_ids.cuda().unsqueeze(0)
                else:
                    input_ids_unsqueezed = input_ids.cpu().unsqueeze(0)
                outputs = torch.softmax(self.model(input_ids_unsqueezed)[-1],axis = -1)[0,:,1]
                preds.append(outputs.cpu().numpy())
        return preds

    def stitch_preds(self, preds: list) -> list:
        return self.sequence_helper.stitch_np_preds(preds)
    
    def label_stitched_preds(self, stitched_preds: list):
        labeled, max_label = scipy.ndimage.label(stitched_preds>self.model_confidence_threshold)
        return labeled, max_label