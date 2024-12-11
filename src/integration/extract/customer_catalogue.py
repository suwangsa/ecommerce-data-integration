import pandas as pd


def extract_customer_catalogue(table: str,engine) -> pd.DataFrame:
    data = pd.read_sql_table(table_name = table,con = engine.connect())
    return data