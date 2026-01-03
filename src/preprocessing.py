import numpy as np

def handle_missing_values(df):
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns

    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

    return df

def scale_features(X, scaler):
    X_scaled = scaler.fit_transform(X)
    return X_scaled

