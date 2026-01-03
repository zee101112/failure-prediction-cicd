from sklearn.utils import resample
import pandas as pd

def oversample_minority(X_train, y_train):
    train = pd.concat([X_train, y_train], axis=1)

    majority = train[train.target == 0]
    minority = train[train.target == 1]

    minority_upsampled = resample(
        minority,
        replace=True,
        n_samples=len(majority),
        random_state=42
    )

    upsampled = pd.concat([majority, minority_upsampled])
    X_up = upsampled.drop('target', axis=1)
    y_up = upsampled['target']

    return X_up, y_up
