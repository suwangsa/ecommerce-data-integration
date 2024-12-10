from src.utils.helper import init_dest_engine
import pandas as pd


def load_process(data: pd.DataFrame, table_name: str, schema_name: str) -> None:

    try:
        conn = init_dest_engine()

        pass

    except Exception as e:
        raise Exception(e)

    finally:
        conn.dispose()
