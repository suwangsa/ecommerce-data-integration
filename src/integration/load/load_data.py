from src.utils.helper import init_dest_engine
import pandas as pd


def load_process(data: pd.DataFrame, table_name: str, schema_name: str) -> None:

    try:
        conn = init_dest_engine()
        data.to_sql(name=table_name,con=conn,if_exists="append",index=False,schema=schema_name)

        pass

    except Exception as e:
        raise Exception(e)

    finally:
        conn.dispose()
