import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from collections import Counter
from datetime import datetime, timezone, timedelta
tzinfo = timezone(timedelta(hours=+7.0))
from __future__ import annotations
import typing
import sqlalchemy as sa
from typing import List
from typing import Optional

from src.recommender.similar_product import similarity_product
from src.recommender.similar_product import get_jaccard_similarity
from src.recommender.related_product import relatable_product
from src.recommender.system import recommender_system
from src.utils.helper import init_engine
from src.utils.helper import init_dest_engine
from src.integration.load import load_data


# RUN
conn = init_dest_engine()
df_rec = recommender_system(42,5,conn)
load_process(data = df_rec, table_name = "ProductRecommendations", schema_name = "dev")