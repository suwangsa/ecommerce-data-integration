from __future__ import annotations
import hashlib
import typing
import sqlalchemy as sa
from typing import List
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
print(sa.__version__ )
# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declarative_base as DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped

# extract
from src.integration.extract.product_catalogue import extract_product_catalogue
from src.integration.extract.campaign_catalogue import extract_campaign_catalogue
from src.integration.extract.customer_catalogue import extract_customer_catalogue
from src.utils.helper import init_engine
from src.utils.helper import init_dest_engine

# transform
from src.integration.transform.category_catalogue import generate_category
from src.integration.transform.product_catalogue import generate_product
from src.integration.transform.tags_catalogue import generate_tags
from src.integration.transform.campaign_catalogue import generate_campaign

# load
from src.integration.load.load_data import load_process
import table_sql

if __name__ == "__main__":
    print("===== Start Data Integration =====\n")

    # EXTRACT
    # extract catalogue
    print("===== Start Extract Catalogue JSON Data, Customer Database, and Campaign Excel Data =====\n")
    df_catalogue_master = extract_product_catalogue(uri = "https://raw.githubusercontent.com/Kurikulum-Sekolah-Pacmann/wrangling-bfp-aksel/refs/heads/main/ecommerce_data/Products.json")
    df_campaign_master = extract_campaign_catalogue(uri = "https://raw.githubusercontent.com/Kurikulum-Sekolah-Pacmann/wrangling-bfp-aksel/refs/heads/main/ecommerce_data/Campaigns.xlsx")
    
    conn = init_engine()
    df_customers = extract_customer_catalogue('customers',conn)
    df_carts = extract_customer_catalogue('carts',conn)
    df_cartitems = extract_customer_catalogue('cartitems',conn)

    print("===== Finished Extract Catalogue JSON Data, Customer Database, and Campaign Excel Data =====\n")
        
    # TRANSFORM    
    df_categories = generate_category(data = df_catalogue_master)
    df_product_catalogue = generate_product(data = df_catalogue_master)
    df_tags = generate_tags(data = df_catalogue_master)
    df_campaigns,df_campaign_items = generate_campaign(data=df_campaign_master)
    

    # LOAD
    load_process(data = df_campaigns, table_name = "campaigns", schema_name = "dev")
    load_process(data = df_campaign_items, table_name = "campaign_items", schema_name = "dev")
    load_process(data = df_categories, table_name = "categories", schema_name = "dev")
    load_process(data = df_customers, table_name = "customers", schema_name = "dev")
    load_process(data = df_carts, table_name = "carts", schema_name = "dev")
    load_process(data = df_product_catalogue, table_name = "products", schema_name = "dev")
    load_process(data = df_tags, table_name = "tags", schema_name = "dev")
    load_process(data = df_cartitems, table_name = "cart_items", schema_name = "dev")

    print("===== Finished Data Integration =====")
