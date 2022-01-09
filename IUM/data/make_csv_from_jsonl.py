import pandas as pd


def make_csv_from_jsonl(json_lines_path, csv_target_path):
    df = pd.read_json(json_lines_path, lines=True)
    df.to_csv(csv_target_path)
