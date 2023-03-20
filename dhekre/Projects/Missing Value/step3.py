# step3.py

from knn import KNNImputerWrapper

def knn_pipeline(df, k=5):
    knn_imputer = KNNImputerWrapper(k)
    imputed_data = knn_imputer.fit_transform(df)
    return imputed_data
