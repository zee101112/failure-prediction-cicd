from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier,
    BaggingClassifier,
    ExtraTreesClassifier
)

from lightgbm import LGBMClassifier
from xgboost import XGBClassifier

def get_models():
    return {
        "RandomForest": RandomForestClassifier(n_estimators=200),
        "GradientBoosting": GradientBoostingClassifier(),
        "AdaBoost": AdaBoostClassifier(),
        "Bagging": BaggingClassifier(),
        "ExtraTrees": ExtraTreesClassifier(),
        "LightGBM": LGBMClassifier(),
        "XGBoost": XGBClassifier(eval_metric="logloss")
    }

