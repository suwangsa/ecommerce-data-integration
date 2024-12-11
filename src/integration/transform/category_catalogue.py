import pandas as pd


def generate_category(data: pd.DataFrame) -> pd.DataFrame:
    df_categories = pd.DataFrame(data['category'].to_list()).drop_duplicates().reset_index(drop=True)[['category_id','name']]
    return df_categories
