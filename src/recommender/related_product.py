import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from collections import Counter
from datetime import datetime, timezone, timedelta
tzinfo = timezone(timedelta(hours=+7.0))

def relatable_products(p,n_result:int,dataset:dict):
    result_list = []
    
    for val in dataset.values():
        if p in val:
            val.remove(p)
            result_list.extend(val)
    
    counter = Counter(result_list)
    
    # formatting
    recommend = list(dict(counter.most_common(n_result)).keys())
    algo    = ['Related Product']*n_result
    id      = [p]*n_result
    calc_date= [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]*n_result

    return {'product_id':id,
            'recommendation_id':recommend,
            'algorithm':algo,
            'calculation_date':calc_date}