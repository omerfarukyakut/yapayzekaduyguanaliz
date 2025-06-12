import pandas as pd
import os

def load_data_from_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return pd.read_csv(file_path)

def load_data_from_database(connection_string, query):
    import sqlite3
    conn = sqlite3.connect(connection_string)
    data = pd.read_sql_query(query, conn)
    conn.close()
    return data

def preprocess_data(data):
    # Örnek ön işleme adımları
    data.dropna(inplace=True)  # Eksik verileri kaldır
    data['text'] = data['text'].str.lower()  # Metni küçük harfe çevir
    return data

def load_and_preprocess_data(source, file_path=None, connection_string=None, query=None):
    if source == 'csv':
        data = load_data_from_csv(file_path)
    elif source == 'database':
        data = load_data_from_database(connection_string, query)
    else:
        raise ValueError("Source must be either 'csv' or 'database'.")
    
    return preprocess_data(data)