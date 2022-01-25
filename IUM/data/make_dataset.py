import os
import logging
from collections import namedtuple
import pandas as pd

from IUM.data.divide_dataset_into_training_and_testing_sets import split_randomly_dataset_into_two_sets
from IUM.data.make_csv_from_jsonl import make_csv_from_jsonl


def process_to_csv() -> None:
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    FileToProcess = namedtuple('FileToProcess', ['relative_input_path', 'relative_output_path'])
    files_to_process = [
        FileToProcess('data/raw/sessions.jsonl', 'data/processed/sessions.csv'),
        FileToProcess('data/raw/products.jsonl', 'data/processed/products.csv')
    ]
    for file_to_process in files_to_process:
        make_csv_from_jsonl(
            make_absolute_path_from_relative(file_to_process.relative_input_path),
            make_absolute_path_from_relative(file_to_process.relative_output_path)
        )


def divide_datasets_into_training_and_testing_set() -> None:
    FileToProcess = namedtuple('FileToProcess', ['relative_input_csv_file_path',
                                                 'training_set_relative_output_csv_file_path',
                                                 'testing_set_relative_output_csv_file_path',
                                                 'ratio'
                                                 ])
    files_to_process = [
        FileToProcess('data/processed/sessions.csv',
                      'data/processed/testing_sessions.csv',
                      'data/processed/training_sessions.csv',
                      0.3
                      )
    ]
    for file_to_process in files_to_process:
        first_dataset, second_dataset = split_randomly_dataset_into_two_sets(
            pd.read_csv(make_absolute_path_from_relative(file_to_process.relative_input_csv_file_path)),
            'session_id',
            file_to_process.ratio)
        first_dataset.to_csv(
            make_absolute_path_from_relative(file_to_process.training_set_relative_output_csv_file_path))
        second_dataset.to_csv(
            make_absolute_path_from_relative(file_to_process.testing_set_relative_output_csv_file_path))


def make_absolute_path_from_relative(relative_path) -> str:
    """This should work automatically, you can also change absolute path with uncommenting first line """
    # return f"{YOUR_PATH_TO_DIR}/relative_path"
    return os.path.join(os.path.dirname(__file__), '../../', relative_path)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    process_to_csv()
    divide_datasets_into_training_and_testing_set()
