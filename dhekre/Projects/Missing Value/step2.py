# step2.py

from mean import MeanImputer

def mean_pipeline(df):
    mean_imputer = MeanImputer()
    imputed_data = mean_imputer.fit_transform(df)
    return imputed_data
