# extract
from src.integration.extract.product_catalogue import extract_catalogue

# transform
from src.integration.transform.category_catalogue import generate_category
from src.integration.transform.product_catalogue import generate_product
from src.integration.transform.tags_catalogue import generate_tags

# load
from src.integration.load.load_data import load_process

if __name__ == "__main__":
    print("===== Start Data Integration =====\n")

    # extract catalogue
    print("===== Start Extract Catalogue JSON Data =====\n")
    df_catalogue_master = extract_catalogue(uri = "https://raw.githubusercontent.com/Kurikulum-Sekolah-Pacmann/wrangling-bfp-aksel/refs/heads/main/ecommerce_data/Products.json")
    
    print("===== Finished Extract Catalogue JSON Data =====\n")
        
    # transform categories
    df_categories = generate_category(data = df_catalogue_master)
    load_process(data = df_categories, table_name = "categories", schema_name = "dev")

    # transform product
    df_product_catalogue = generate_product(data = df_catalogue_master)
    load_process(data = df_product_catalogue, table_name = "product_catalogue", schema_name = "dev")

    # transform tags
    df_tags = generate_tags(data = df_catalogue_master)
    load_process(data = df_tags, table_name = "tags", schema_name = "dev")

    print("===== Finished Data Integration =====")
