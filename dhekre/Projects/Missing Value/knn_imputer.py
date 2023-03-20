from typing import List, Tuple
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer


class KNNImputerHandler:
    def __init__(self, k: int = 5):
        self.k = k
        self.imputer = KNNImputer(n_neighbors=k)

    def fit_transform(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, np.ndarray]:
        imputed_data = self.imputer.fit_transform(data)
        df_imputed = pd.DataFrame(imputed_data, columns=data.columns)
        missing_mask = data.isnull().values
        imputed_mask = np.isnan(imputed_data)
        missing_values_imputed = imputed_mask & missing_mask
        return df_imputed, missing_values_imputed
