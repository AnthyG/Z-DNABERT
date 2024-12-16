import os
import pathlib
import argparse
from tqdm.auto import tqdm
import logging
from src.prediction_runner import PredictionRunner
from src.prediction_input import PredictionInput
from src.prediction_input_file_from_filesystem import PredictionInputFileFromFilesystem
from src.zdnabert_model import ZdnabertModel
from src.sequence_variation_normal import SequenceVariationNormal
from src.sequence_variation_reverse_complement import SequenceVariationReverseComplement
from src.prediction_result_formatter_bed_file import PredictionResultFormatterBedFile
from src.zdnabert_model_downloader import ZdnabertModelDownloader

# Define default paths
MODEL_DOWNLOAD_PATH = './pytorch_models'
INPUT_PATH = './input'
OUTPUT_PATH = './output'

# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Run Z-DNABERT predictions on input sequences.")
    parser.add_argument(
    '--model',
    type=str,
    required=True,
    choices=["HG_chipseq", "HG_kouzine", "MM_chipseq", "MM_kouzine"],
    help="Name of the model to use. Choices are: HG_chipseq, HG_kouzine, MM_chipseq, MM_kouzine."
)

    parser.add_argument('--confidence-threshold', type=float, default=0.5, help="Model confidence threshold.")
    parser.add_argument('--min-seq-length', type=int, default=10, help="Minimum sequence length to process.")
    parser.add_argument('--check-reverse-complement', action='store_true', help="Check reverse complement sequence variations.")
    parser.add_argument('--use-cuda', action='store_true', help="Use CUDA if available.")
    parser.add_argument('--input', type=str, default=INPUT_PATH, help="Path to input files.")
    parser.add_argument('--output', type=str, default=OUTPUT_PATH, help="Path to save output files.")
    args = parser.parse_args()

    # Prepare paths
    input_path = pathlib.Path(args.input)
    output_path = pathlib.Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)

    # Download and initialize the model
    zdnabert_model_downloader = ZdnabertModelDownloader()
    zdnabert_model_downloader.download_models(MODEL_DOWNLOAD_PATH)
    zdnabert_model_downloader.download_metas(MODEL_DOWNLOAD_PATH)

    zdnabert_model = ZdnabertModel(
        os.path.join(MODEL_DOWNLOAD_PATH, args.model),
        model_name=args.model,
        model_confidence_threshold=args.confidence_threshold,
        minimum_sequence_length=args.min_seq_length,
        use_cuda_if_available=args.use_cuda,
    )

    # Initialize sequence variations
    sequence_variations = [SequenceVariationNormal()]
    if args.check_reverse_complement:
        sequence_variations.append(SequenceVariationReverseComplement())

    # Prepare input files
    prediction_input_files = []
    for file_path in input_path.iterdir():
        if file_path.is_file():
            prediction_input_files.append(
                PredictionInputFileFromFilesystem(file_path.name, file_path)
            )

    prediction_input = PredictionInput(
        zdnabert_model,
        prediction_input_files,
        sequence_variations,
    )

    prediction_inputs = [prediction_input]
    prediction_result_formatter_bed_file = PredictionResultFormatterBedFile()
    prediction_runner = PredictionRunner()

    # Run predictions and save outputs
    for prediction_result in prediction_runner.run(prediction_inputs, progress_bar=tqdm):
        bed_file_name = prediction_result_formatter_bed_file.file_name(prediction_result)
        output_file_path = output_path / bed_file_name

        with open(output_file_path, 'w') as bed_file:
            for line in prediction_result_formatter_bed_file.format(prediction_result):
                bed_file.write(f"{line}\n")

        print(f"Results saved to {output_file_path}")

if __name__ == "__main__":
    main()
