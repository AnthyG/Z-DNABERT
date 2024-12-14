import os
import pathlib
from src.model_manager import ModelManager
from src.model_downloader_google_drive import ModelDownloaderGoogleDrive

class ZdnabertModelDownloader():
    models = {
        'HG_kouzine': (
            '1dAeAt5Gu2cadwDhbc7OnenUgDLHlUvkx',
            'hg_kouzine.pytorch_model.bin',
        ),
        'HG_chipseq': (
            '1VAsp8I904y_J0PUhAQqpSlCn1IqfG0FB',
            'hg_chipseq.pytorch_model.bin',
        ),
        'MM_curax': (
            '1W6GEgHNoitlB-xXJbLJ_jDW4BF35W1Sd',
            'mm_curax.pytorch_model.bin',
        ),
        'MM_kouzine': (
            '1dXpQFmheClKXIEoqcZ7kgCwx6hzVCv3H',
            'mm_kouzine.pytorch_model.bin',
        ),
    }
    
    meta_files = [
        ('10sF8Ywktd96HqAL0CwvlZZUUGj05CGk5', 'config.json'),
        ('16bT7HDv71aRwyh3gBUbKwign1mtyLD2d', 'special_tokens_map.json'),
        ('1EE9goZ2JRSD8UTx501q71lGCk-CK3kqG', 'tokenizer_config.json'),
        ('1gZZdtAoDnDiLQqjQfGyuwt268Pe5sXW0', 'vocab.txt'),
    ]
    
    def __init__(self):
        self.model_downloader_google_drive = ModelDownloaderGoogleDrive()
        self.model_manager = ModelManager()
    
    def download_models(self, download_path: str):
        for model_name in self.models:
            model_gdrive_id, model_file_name = self.models[model_name]
            model_file_path = os.path.join(download_path, model_name, 'pytorch_model.bin')
            pathlib.Path(os.path.join(download_path, model_name)).mkdir(parents=True, exist_ok=True)
            self.model_downloader_google_drive.download(model_gdrive_id, model_file_path)

    def download_metas(self, download_path: str):
        for meta_file_gdrive_id, meta_file_name in self.meta_files:
            meta_file_path = os.path.join(download_path, meta_file_name)
            pathlib.Path(os.path.join(download_path)).mkdir(parents=True, exist_ok=True)
            self.model_downloader_google_drive.download(meta_file_gdrive_id, meta_file_path)
            for model_name in self.models:
                meta_file_path_copy = os.path.join(download_path, model_name, meta_file_name)
                pathlib.Path(os.path.join(download_path, model_name)).mkdir(parents=True, exist_ok=True)
                self.model_manager.copy_file(meta_file_path, meta_file_path_copy)
