import pandas as pd

def query_data():
    df = pd.read_csv('query/q_blue.csv')
    df['max'] = max(df['timestamp'])
    df_list = df.values.tolist()
    return df_list
