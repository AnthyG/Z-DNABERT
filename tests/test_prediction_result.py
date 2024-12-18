import unittest
from unittest.mock import Mock

from src.prediction_result import PredictionResult
from src.sequence_variation import SequenceVariation


class TestPredictionResult(unittest.TestCase):

    def test_get_model_params_as_string(self):
        model_name = 'MODEL_NAME'
        model_confidence_threshold = 0.25
        minimum_sequence_length = 12
        sequence_variation_mock = Mock(spec=SequenceVariation)

        prediction_result = PredictionResult(
            model_name,
            model_confidence_threshold,
            minimum_sequence_length,
            '',
            '',
            sequence_variation_mock,
            0,
            None,
            0
        )

        actual = prediction_result.get_model_params_as_string()

        self.assertEqual(
            actual,
            'm={},mct={},msl={}'.format(model_name, model_confidence_threshold, minimum_sequence_length)
        )

    def test_get_model_params_as_string_for_file_name(self):
        model_name = 'MODEL_NAME'
        model_confidence_threshold = 0.25
        minimum_sequence_length = 12
        
        prediction_result = PredictionResult(
            model_name,
            model_confidence_threshold,
            minimum_sequence_length,
            '',
            '',
            None,
            0,
            None,
            0
        )

        actual = prediction_result.get_model_params_as_string_for_file_name()

        self.assertEqual(
            actual,
            'm_{},mct_{},msl_{}'.format(model_name, model_confidence_threshold, minimum_sequence_length)
        )

if __name__ == '__main__':
    unittest.main()
