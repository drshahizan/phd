# step1.py

from cold_deck import ColdDeckImputer

def cold_deck_pipeline(df, reference_data):
    cold_deck_imputer = ColdDeckImputer(reference_data)
    imputed_data = cold_deck_imputer.fit_transform(df)
    return imputed_data
