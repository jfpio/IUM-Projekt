import os
from random import seed

import pandas as pd

from IUM.data.divide_dataset_into_training_and_testing_sets import split_randomly_dataset_into_two_sets
from IUM.data.get_user_sessions_bought_to_all_sessions_ratio import \
    get_user_sessions_bought_to_all_sessions_ratio_and_save_to_json
from IUM.data.make_csv_from_jsonl import make_csv_from_jsonl
from IUM.data.prepare_data_to_model import prepare_data_to_model


def process_data():
    seed(0)
    make_csv_from_jsonl(
        make_absolute_path_from_relative('data/raw/sessions.jsonl'),
        make_absolute_path_from_relative('data/processed/sessions.csv')
    )

    all_sessions = pd.read_json(make_absolute_path_from_relative('data/raw/sessions.jsonl'), lines=True)

    training_set, testing_set = split_randomly_dataset_into_two_sets(
        all_sessions,
        attribute_to_group_by='session_id',
        divide_ratio=0.3
    )
    ratio = get_user_sessions_bought_to_all_sessions_ratio_and_save_to_json(
        all_sessions,
        make_absolute_path_from_relative('data/processed/session_ratio_per_user.json')
    )

    training_data = prepare_data_to_model(training_set, ratio)
    testing_data = prepare_data_to_model(testing_set, ratio)
    training_data.to_csv(make_absolute_path_from_relative('data/processed/testing_set'))
    testing_data.to_csv(make_absolute_path_from_relative('data/processed/training_set'))


def make_absolute_path_from_relative(relative_path) -> str:
    """This should work automatically, you can also change absolute path with uncommenting first line """
    # return f"{YOUR_PATH_TO_DIR}/relative_path"
    return os.path.join(os.path.dirname(__file__), '../../', relative_path)


process_data()
