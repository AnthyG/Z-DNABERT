import os
import subprocess
import logging

class ModelManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def copy_file(self, source_path: str, target_path: str):
        hash1 = self.hash_file(source_path)
        hash2 = self.hash_file(target_path)
        if hash1 != hash2:
            self.logger.info('\ncopying file to input directory\n')
            subprocess.run(['cp', source_path, target_path])
        else:
            self.logger.info('\nfile hasn\'t changed\n')
    
    def hash_file(self, file_path: str):
        if os.path.exists(file_path) == False:
            return None
        
        return subprocess.run(['shasum', file_path], stdout=subprocess.PIPE).stdout[:40]
