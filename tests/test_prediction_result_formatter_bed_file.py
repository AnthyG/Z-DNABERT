import unittest
from unittest.mock import Mock

from src.sequence_variation import SequenceVariation
from src.prediction_result_formatter_bed_file import PredictionResultFormatterBedFile
from src.prediction_result import PredictionResult

class TestPredictionResultFormatterBedFile(unittest.TestCase):

    cls: PredictionResultFormatterBedFile
    
    def setUp(self):
        self.cls = PredictionResultFormatterBedFile()
    
    def test_file_name_common(self):
        model_params = 'a_MODEL_PARAMS,b_0.25,c_12'
        file_name = 'FILE_NAME'
        seq_record_name = 'SEQUENCE_RECORD_NAME'
        sequence_variation_mock = Mock(spec=SequenceVariation)
        now_time_as_string_for_file_name = '2024_12_31,09_45_59'

        prediction_result = PredictionResult(
            '',
            0.0,
            0,
            file_name,
            seq_record_name,
            sequence_variation_mock,
            0,
            None,
            0,
        )
        prediction_result.get_model_params_as_string_for_file_name = Mock(return_value=model_params)

        actual = self.cls.file_name_common(prediction_result, now_time_as_string_for_file_name)

        self.assertRegex(
            actual,
            '{file_name}.{seq_record_name}.{model_params}.{now_time_as_string_for_file_name}.bed'.format(
                file_name=file_name,
                seq_record_name=seq_record_name,
                model_params=model_params,
                now_time_as_string_for_file_name=now_time_as_string_for_file_name,
            )
        )

    def test_file_name_variation(self):
        model_params = 'a_MODEL_PARAMS,b_0.25,c_12'
        file_name = 'FILE_NAME'
        seq_record_name = 'SEQUENCE_RECORD_NAME'
        sequence_variation_title = 'SEQUENCE_VARIATION_TITLE'
        sequence_variation_mock = Mock(spec=SequenceVariation)
        sequence_variation_mock.get_title = Mock(return_value=sequence_variation_title)
        now_time_as_string_for_file_name = '2024_12_31,09_45_59'

        prediction_result = PredictionResult(
            '',
            0.0,
            0,
            file_name,
            seq_record_name,
            sequence_variation_mock,
            0,
            None,
            0,
        )
        prediction_result.get_model_params_as_string_for_file_name = Mock(return_value=model_params)

        actual = self.cls.file_name_variation(prediction_result, now_time_as_string_for_file_name)

        self.assertRegex(
            actual,
            '{file_name}.{seq_record_name}.{model_params}.{now_time_as_string_for_file_name}.{sequence_variation_title}.bed'.format(
                file_name=file_name,
                seq_record_name=seq_record_name,
                model_params=model_params,
                now_time_as_string_for_file_name=now_time_as_string_for_file_name,
                sequence_variation_title=sequence_variation_title,
            )
        )

if __name__ == '__main__':
    unittest.main()
