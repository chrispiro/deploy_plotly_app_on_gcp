import pandas as pd
from google.cloud import bigquery
from google.cloud import storage

def load_data_from_bigquery(project, dataset, table):
    '''
    Read the first half of the dataset from BigQuery
    '''

    #TODO: Write the code to load the data from BigQuery

    # Construct a BigQuery client object.
    bqclient = bigquery.Client()

    #project = coo-risk-ews-d
    #datest = code_breakfast
    #table = world_population_1

    query = """
        SELECT * from `{}.{}.{}`
    """.format(project, dataset, table)
    
    df1 = (
        bqclient.query(query)
        .result()
        .to_dataframe()
    )

    return df1

def load_data_from_cloudstorage(bucket, blob):
    '''
    Read the second half of the dataset from GCS
    '''

    #TODO: Write the code to load the data from GCS

    #bucket = code_breakfast
    #blob = world_population_2.csv
    gcs_path = 'gs://{}/{}'.format(bucket, blob)

    df2 = pd.read_csv(gcs_path, sep=';')

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