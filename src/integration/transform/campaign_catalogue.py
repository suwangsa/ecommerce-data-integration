import pandas as pd


def generate_campaign(data: pd.DataFrame) -> pd.DataFrame:
    df_campaigns = data[['campaign_id','name','campaign_type','start_date']]
    df_campaign_items = data[['campaign_id','campaign_type','campaign_objects']].copy()
    df_campaign_items['campaign_objects'] = df_campaign_items['campaign_objects'].map(lambda x:x.split(';'))
    df_campaign_items = df_campaign_items.explode('campaign_objects').reset_index(drop=True)
    cat_mapper = dict(zip(table_categories['category_id'],table_categories['name']))
    prd_mapper = dict(zip(df_products['product_id'],df_products['name']))
    df_campaign_items['campaign_item'] = [cat_mapper[int(i[2])] if i[1]=='Category' else prd_mapper[int(i[2])] for i in df_campaign_items[['campaign_type','campaign_objects']].itertuples()]
    df_campaign_items = df_campaign_items.reset_index(names='campaign_item_id').drop(columns=['campaign_objects'])
    df_campaign_items
    
    return df_campaigns,df_campaign_items