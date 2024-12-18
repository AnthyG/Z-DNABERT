import unittest
from unittest.mock import Mock

from src.sequence_variation import SequenceVariation
from src.prediction_result_formatter_bed_file import PredictionResultFormatterBedFile
from src.prediction_result import PredictionResult

class TestPredictionResultFormatterBedFile(unittest.TestCase):

    cls: PredictionResultFormatterBedFile
    
    def setUp(self):
        self.cls = PredictionResultFormatterBedFile()
    
    def test_file_name(self):
        model_params = 'a_MODEL_PARAMS,b_0.25,c_12'
        file_name = 'FILE_NAME'
        seq_record_name = 'SEQUENCE_RECORD_NAME'
        sequence_variation_title = 'SEQUENCE_VARIATION_TITLE'
        sequence_variation_mock = Mock(spec=SequenceVariation)
        sequence_variation_mock.get_title = Mock(return_value=sequence_variation_title)

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

        actual = self.cls.file_name(prediction_result)

        self.assertRegex(
            actual,
            '\d{4}_\d{2}_\d{2}\,\d{2}_\d{2}_\d{2}'
        )

        self.assertRegex(
            actual,
            '{file_name}.{seq_record_name}.{model_params}.'.format(
                file_name=file_name,
                seq_record_name=seq_record_name,
                model_params=model_params,
            ) +
            '\d{4}_\d{2}_\d{2},\d{2}_\d{2}_\d{2}' +
            '.{sequence_variation_title}.bed'.format(
                sequence_variation_title=sequence_variation_title,
            )
        )

if __name__ == '__main__':
    unittest.main()
