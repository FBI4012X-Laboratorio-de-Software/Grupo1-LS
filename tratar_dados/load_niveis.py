import pandas as pd


def load_niveis_data() -> dict:

    with open('.niveis', 'r') as file:
        data_frame = pd.read_csv(file)

    return data_frame.to_dict()
