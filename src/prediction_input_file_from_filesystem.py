from src.prediction_input_file import PredictionInputFile

class PredictionInputFileFromFilesystem(PredictionInputFile):
    file_handler = None
    
    def __init__(self, file_path: str):
        self.file_path = file_path

    def open(self):
        self.file_handler = open(self.file_path, 'r', encoding='utf-8')
        return self.file_handler

    def close(self):
        self.file_handler.close()
        self.file_handler = None