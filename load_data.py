import pandas as pd

def load_data_from_bigquery():
    return None
def load_data_from_cloudstorage():
    return None

def load_local_data(local_path):
    df = pd.read_csv(local_path)

    return df