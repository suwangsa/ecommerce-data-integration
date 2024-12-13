import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from collections import Counter
from datetime import datetime, timezone, timedelta
tzinfo = timezone(timedelta(hours=+7.0))

def recommender_system(id,n_result:int,engine):
    df_cartitems = pd.read_sql_table(table_name = 'cart_items',con = engine.connect())
    df_tags = pd.read_sql_table(table_name = 'tags',con = engine.connect())
    engine.dispose()

    df_tags['tag_id'] = df_tags['tag_id'].map(lambda x:x.split('-')[-1])
    tag_dict = df_tags.groupby('product_id')['tag_id'].agg(list).to_dict()
    cart_dict = df_cartitems.groupby('cart_id')['product_id'].agg(list).to_dict()

    d1 = similarity_products(id, n_result, dataset=tag_dict)
    d2 = relatable_products(id,n_result, dataset=cart_dict)

    return pd.concat([pd.DataFrame(d1),pd.DataFrame(d2)],ignore_index=True)
