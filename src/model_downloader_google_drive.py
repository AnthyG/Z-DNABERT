import os
import subprocess
import logging

class ModelDownloaderGoogleDrive:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def download(self, gdrive_id: str, file_path: str):
        if os.path.exists(file_path):
            self.logger.info(file_path, gdrive_id, 'already exists')
            return
        
        # curl "https://drive.google.com/uc?id=${id}&export=download&confirm=ABCD" --verbose -L -o 
        #gdrive_url = 'https://drive.google.com/uc?id={id}&export=download&confirm=ABCD'.format(id=gdrive_id)
        gdrive_url = 'https://drive.usercontent.google.com/download?id={id}&confirm=ABCD'.format(id=gdrive_id)
        
        self.logger.info(gdrive_url, file_path)
        
        #curl -L --progress-bar -o "{file_path}" "{gdrive_url}"
        
        subprocess.run(['curl', '-L', '--progress-bar', '-o', file_path, gdrive_url])
