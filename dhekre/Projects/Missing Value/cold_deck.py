import sys
print(sys.executable)

import pandas as pd

class ColdDeckImputer:
    def __init__(self, reference_data):
        self.reference_data = reference_data
        self.imputed_data = None

    def fit(self, data):
        self.imputed_data = data.copy()
        for col in self.imputed_data.columns:
            self.imputed_data[col].fillna(self.reference_data[col], inplace=True)

    def transform(self, data):
        imputed_data = data.copy()
        for col in imputed_data.columns:
            imputed_data[col].fillna(self.reference_data[col], inplace=True)
        return imputed_data

    def fit_transform(self, data):
        self.fit(data)
        return self.imputed_data
