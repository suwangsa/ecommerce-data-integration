import pandas as pd


def generate_product(data: pd.DataFrame) -> pd.DataFrame:
    df_products = data[['product_id', 'name', 'price', 'description', 'category', 'image_url']]
    df_products['category'] = df_products['category'].map(lambda x:x['category_id'])
    df_products.rename(columns={'category':'category_id'},inplace=True)
    return df_products
