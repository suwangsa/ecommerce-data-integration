import pandas as pd


def generate_tags(data: pd.DataFrame) -> pd.DataFrame:
    df_tags = data[['product_id','tags']]
    tag_index = {value:str(key+1) for key,value in enumerate(sorted(df_tags.explode('tags')['tags'].unique()))}
    df_tags = df_tags.explode('tags').reset_index(drop=True)
    df_tags['tag_id'] = df_tags['product_id'].astype('str')
    df_tags['tag_id'] = df_tags['tag_id'] +"-"+ df_tags['tags'].map(tag_index)
    df_tags = df_tags.rename(columns={'tags':'tag'})
    return df_tags[['tag_id','tag','product_id']]
