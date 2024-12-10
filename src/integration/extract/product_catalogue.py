import pandas as pd


def extract_catalogue(uri: str) -> pd.DataFrame:
    data = pd.read_json(uri)

    return data
