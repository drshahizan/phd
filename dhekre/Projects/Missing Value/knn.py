# knn.py

import pandas as pd
from sklearn.impute import KNNImputer

class KNNImputerWrapper:
    def __init__(self, k=5):
        self.k = k
        self.imputer = KNNImputer(n_neighbors=k)
        self.imputed_data = None

    def fit(self, data):
        self.imputer.fit(data)

    def transform(self, data):
        self.imputed_data = pd.DataFrame(self.imputer.transform(data), columns=data.columns)
        return self.imputed_data

    def fit_transform(self, data):
        self.imputed_data = pd.DataFrame(self.imputer.fit_transform(data), columns=data.columns)
        return self.imputed_data
