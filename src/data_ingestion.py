import pandas as pd

def load_sample(filepath, nrows=100000, sep=';'):
    df_sample = pd.read_csv(filepath, sep=sep, nrows=nrows)
    print(f"Loaded sample shape: {df_sample.shape}")
    return df_sample

def load_full(filepath, sep=';'):
    df = pd.read_csv(filepath, sep=sep)
    print(f"Full dataset shape: {df.shape}")
    return df
