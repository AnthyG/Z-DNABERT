import unittest
from unittest.mock import Mock

from src.prediction_runner import PredictionRunner
from src.zdnabert_model import ZdnabertModel
from src.prediction_input import PredictionInput
from src.prediction_input_file import PredictionInputFile
from src.prediction_result import PredictionResult
from src.sequence_variation import SequenceVariation

class TestPredictionRunner(unittest.TestCase):

    def test_run(self):
        model_mock = Mock(spec=ZdnabertModel)
        prediction_input_file_mock_1 = Mock(spec=PredictionInputFile)
        prediction_input_file_mock_2 = Mock(spec=PredictionInputFile)
        sequence_variation_mock_1 = Mock(spec=SequenceVariation)
        sequence_variation_mock_2 = Mock(spec=SequenceVariation)
        prediction_input_1 = PredictionInput(
            model_mock,
            [prediction_input_file_mock_1, prediction_input_file_mock_2],
            [sequence_variation_mock_1, sequence_variation_mock_2]
        )

        prediction_runner = PredictionRunner()

        prediction_runner.run([prediction_input_1])

if __name__ == '__main__':
    unittest.main()
