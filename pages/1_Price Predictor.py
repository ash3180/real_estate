import streamlit as st
import pickle
import gzip
import os
import pandas as pd
import numpy as np

# Patch scikit-learn unpickling compatibility for ColumnTransformer if using newer sklearn version
try:
    import sklearn.compose._column_transformer
    class _RemainderColsList(list):
        pass
    sklearn.compose._column_transformer._RemainderColsList = _RemainderColsList
except Exception:
    pass

st.set_page_config(page_title="Price Predictor | Gurgaon Real Estate", page_icon="💰", layout="wide")

st.title("💰 Property Price Predictor")
st.markdown("Enter property details below to estimate market valuation for properties across Gurgaon.")

@st.cache_resource
def load_data_and_model():
    with open('df.pkl', 'rb') as file:
        df = pickle.load(file)
    
    # Load compressed model pipeline if available, fallback to uncompressed
    if os.path.exists('pipeline.pkl.gz'):
        with gzip.open('pipeline.pkl.gz', 'rb') as file:
            pipeline = pickle.load(file)
    elif os.path.exists('pipeline.pkl'):
        with open('pipeline.pkl', 'rb') as file:
            pipeline = pickle.load(file)
    else:
        raise FileNotFoundError("Model file (pipeline.pkl.gz or pipeline.pkl) not found.")
        
    return df, pipeline

df, pipeline = load_data_and_model()

st.subheader("📋 Property Specifications")

col1, col2, col3 = st.columns(3)

with col1:
    property_type = st.selectbox('Property Type', ['flat', 'house'])
    sector = st.selectbox('Sector / Location', sorted(df['sector'].unique().tolist()))
    bedrooms = float(st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))
    bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))

with col2:
    balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
    property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))
    built_up_area = float(st.number_input('Built Up Area (Sq. Ft.)', min_value=100.0, value=1500.0, step=50.0))
    furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))

with col3:
    luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
    floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))
    servant_room = float(st.selectbox('Servant Room', [0.0, 1.0], format_func=lambda x: 'Yes' if x == 1.0 else 'No'))
    store_room = float(st.selectbox('Store Room', [0.0, 1.0], format_func=lambda x: 'Yes' if x == 1.0 else 'No'))

st.markdown("---")

if st.button('🚀 Predict Price', type="primary", use_container_width=True):
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']
    
    one_df = pd.DataFrame(data, columns=columns)

    with st.spinner("Calculating estimated price range..."):
        base_price = np.expm1(pipeline.predict(one_df))[0]
        low = max(0.1, base_price - 0.22)
        high = base_price + 0.22

    st.success("### Estimated Price Valuation")
    
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric(label="Estimated Valuation", value=f"₹ {round(base_price, 2)} Cr")
    with res_col2:
        st.metric(label="Estimated Range", value=f"₹ {round(low, 2)} Cr - ₹ {round(high, 2)} Cr")

    with st.expander("🔍 View Submitted Input Parameters"):
        st.dataframe(one_df, use_container_width=True)
