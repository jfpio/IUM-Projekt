import random
from typing import Tuple

import pandas as pd


def split_randomly_dataset_into_two_sets(dataset: pd.DataFrame,
                                         attribute_to_group_by,
                                         divide_ratio,
                                         ) -> Tuple[pd.DataFrame, pd.DataFrame]:
    unique_values = dataset[attribute_to_group_by].unique()
    random.shuffle(unique_values)
    boundary_value = int(round(divide_ratio * len(unique_values)))
    first_set_ids = unique_values[:boundary_value]
    second_set_ids = unique_values[boundary_value:]
    return (
        dataset[dataset[attribute_to_group_by].isin(first_set_ids)],
        dataset[dataset[attribute_to_group_by].isin(second_set_ids)]
    )
