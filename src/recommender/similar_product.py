import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from collections import Counter
from datetime import datetime, timezone, timedelta
tzinfo = timezone(timedelta(hours=+7.0))

def get_jaccard_similarity(a:list,b:list):
    c = set(a).intersection(set(b))
    return float(len(c))/(len(a)+len(b)-len(c))

def similarity_products(p, n_result:int, dataset:dict):
    result_dict = dict()
    timer_dict = dict()
    for k,v in dataset.items():
        if v == dataset[p]:
            continue
        else:
            result_dict[k] = get_jaccard_similarity(dataset[p],v)
            timer_dict[k] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    counter = Counter(result_dict)

    # formatting
    recommend = list(dict(counter.most_common(n_result)).keys())
    algo    = ['Similar Product']*n_result
    id      = [p]*n_result
    calc_date= [timer_dict[key] for key in recommend]

    return {'product_id':id,
            'recommendation_id':recommend,
            'algorithm':algo,
            'calculation_date':calc_date}
