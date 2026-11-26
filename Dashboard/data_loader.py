from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent

@st.cache_data
def load_data():
    raw = pd.read_csv(ROOT / 'Dataset/customer_booking.csv', encoding='latin1')
    clustered = pd.read_csv(ROOT / 'Unsupervised_Learning/clustered_data.csv')
    processed = pd.read_csv(ROOT / 'Dataset/preprocessed_data.csv')
    ids = clustered['row_id']
    if len(raw) != len(processed) or len(clustered) != len(raw) or ids.duplicated().any() or set(ids) != set(range(len(raw))):
        raise ValueError('Cluster row identifiers do not cover the original dataset exactly.')
    c = clustered.set_index('row_id').sort_index()
    cols = [x for x in processed if x != 'data_split']
    if not np.allclose(c[cols].to_numpy(float), processed[cols].to_numpy(float), rtol=1e-7, atol=1e-8):
        raise ValueError('Cluster records do not match the saved preprocessed records.')
    train = processed['data_split'].eq('train')
    check = raw.copy()
    check['total_extra_services'] = check[['wants_extra_baggage','wants_preferred_seat','wants_in_flight_meals']].sum(axis=1)
    for col in ['route', 'booking_origin']:
        check[col] = raw[col].map(raw.loc[train, col].value_counts(normalize=True)).fillna(0)
    for col in ['num_passengers','purchase_lead','length_of_stay','flight_hour','flight_duration','total_extra_services']:
        check[col] = (check[col] - check.loc[train, col].mean()) / check.loc[train, col].std(ddof=0)
    check = pd.get_dummies(check, columns=['sales_channel','trip_type','flight_day'], dtype=float).reindex(columns=cols, fill_value=0)
    if not np.allclose(check.to_numpy(float), processed[cols].to_numpy(float), rtol=1e-6, atol=1e-7):
        raise ValueError('Original records could not be verified against the training transformations; segmentation is unavailable.')
    raw['cluster'] = c['cluster'].to_numpy()
    return raw, c

@st.cache_data
def load_importance():
    return pd.read_csv(ROOT / 'Supervised_Learning/evaluation_results/model1_feature_importance.csv')
