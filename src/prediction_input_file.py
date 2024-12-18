class PredictionInputFile:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def open(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()
