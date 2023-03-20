# main.py

import pandas as pd
from step1 import cold_deck_pipeline
from step2 import mean_pipeline
from step3 import knn_pipeline
from cold_deck import ColdDeck
from mean_imputation import MeanImputation
from knn_imputation import KNNImputation
from evaluate_models import evaluate_models

# Load data
df = pd.read_csv('thyroid.csv')

# Step 1: Cold-deck imputation
reference_data = pd.read_csv('reference_data.csv')
df = cold_deck_pipeline(df, reference_data)

# Step 2: Mean imputation
df = mean_pipeline(df)

# Step 3: K-NN imputation
df = knn_pipeline

# Initialize the imputation classes
cd = ColdDeck()
mi = MeanImputation()
knn = KNNImputation()

# Perform cold-deck imputation
df_cd = cd.impute(df)

# Perform mean imputation
df_mean = mi.impute(df)

# Perform K-NN imputation
df_knn = knn.impute(df)

# Evaluate the models
evaluate_models(df_cd, df_mean, df_knn)
