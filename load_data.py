import pandas as pd
from google.cloud import bigquery
from google.cloud import storage

def load_data_from_bigquery(project, dataset, table):
    '''
    Read the first half of the dataset from BigQuery
    '''

    #TODO: Write the code to load the data from BigQuery


    return df1

def load_data_from_cloudstorage(bucket, blob):
    '''
    Read the second half of the dataset from GCS
    '''

    #TODO: Write the code to load the data from GCS

    return df2

def combine_dataframes(df1,df2):
    '''
    Combine the two dataframe from BigQuery and GCS 
    '''

    return df1.append(df2)


def load_local_data(local_path):
    '''
    Read .csv file from local_path
    '''
    
    df = pd.read_csv(local_path)

    return df