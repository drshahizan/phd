# mean.py

import pandas as pd

class MeanImputer:
    def __init__(self):
        self.mean_values = None

    def fit(self, data):
        self.mean_values = data.mean()

    def transform(self, data):
        return data.fillna(self.mean_values)

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)
