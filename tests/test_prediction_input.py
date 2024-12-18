import unittest
from unittest.mock import Mock

from src.prediction_input import PredictionInput
from src.prediction_input_file import PredictionInputFile
from src.sequence_variation import SequenceVariation
from src.zdnabert_model import ZdnabertModel


class TestPredictionInput(unittest.TestCase):

    def test_instantiation(self):
        model_mock = Mock(spec=ZdnabertModel)
        prediction_input_file_mock_1 = Mock(spec=PredictionInputFile)
        prediction_input_file_mock_2 = Mock(spec=PredictionInputFile)
        sequence_variation_mock_1 = Mock(spec=SequenceVariation)
        sequence_variation_mock_2 = Mock(spec=SequenceVariation)
        
        actual = PredictionInput(
            model_mock,
            [prediction_input_file_mock_1, prediction_input_file_mock_2],
            [sequence_variation_mock_1, sequence_variation_mock_2]
        )

        self.assertIsInstance(actual, PredictionInput)

if __name__ == '__main__':
    unittest.main()
