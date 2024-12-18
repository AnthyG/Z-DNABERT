import unittest
from unittest.mock import Mock

from src.create_progress_bar import create_progress_bar
from src.prediction_input import PredictionInput
from src.prediction_input_file import PredictionInputFile
from src.prediction_runner import PredictionRunner
from src.sequence_variation import SequenceVariation
from src.zdnabert_model import ZdnabertModel


class TestPredictionRunner(unittest.TestCase):

    def test_run(self):
        self.skipTest('need to mock more')

        model_mock = Mock(spec=ZdnabertModel)
        prediction_input_file_mock_1 = Mock(spec=PredictionInputFile)
        file_name_1 = 'FILE_NAME_1'
        prediction_input_file_mock_1.file_name = file_name_1
        prediction_input_file_mock_2 = Mock(spec=PredictionInputFile)
        file_name_2 = 'FILE_NAME_2'
        prediction_input_file_mock_2.file_name = file_name_2
        sequence_variation_mock_1 = Mock(spec=SequenceVariation)
        sequence_variation_mock_2 = Mock(spec=SequenceVariation)
        
        prediction_input_1 = PredictionInput(
            model_mock,
            [prediction_input_file_mock_1, prediction_input_file_mock_2],
            [sequence_variation_mock_1, sequence_variation_mock_2]
        )

        prediction_runner = PredictionRunner()

        actual = prediction_runner.run([prediction_input_1], create_progress_bar(disable=True))
        actual_array = [v for v in actual]

        self.assertEqual(2, len(actual_array))

if __name__ == '__main__':
    unittest.main()
