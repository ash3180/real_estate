# 🏡 Gurgaon Real Estate Analytics, Price Prediction & Recommendation Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Plotly](https://img.shields.io/badge/Plotly-239120?style=flat&logo=plotly&logoColor=white)](https://plotly.com/)

An end-to-end Machine Learning web application designed to analyze real estate data across Gurgaon, predict property valuation using trained ML pipelines, and provide content-based property recommendations.

---

## 🌟 Key Features

1. **🏡 Interactive Landing Portal (`Home.py`)**
   - Overview of key metrics, sector coverage, ML model details, and navigation links.

2. **💰 Property Price Predictor (`pages/1_Price Predictor.py`)**
   - Predict estimated market value in **₹ Crores** based on inputs like sector, bedrooms, bathrooms, built-up area, property age, furnishing type, luxury score, and floor category.
   - Built with a Scikit-Learn `Pipeline` using ensemble tree regression algorithms trained on log-transformed price targets.
   - Includes automatic backward-compatibility patches for unpickling `ColumnTransformer` across different `scikit-learn` versions.

3. **📊 Real Estate Analytics Dashboard (`pages/2_Analysis App.py`)**
   - **Geographic Sector Map**: Interactive Mapbox plot displaying average price per sq. ft. across sectors.
   - **Area vs. Price Scatter Plots**: Price progression based on built-up area and BHK configuration.
   - **BHK Breakdown & Box Plots**: Pie charts and price range distributions across 1-4+ BHK properties.
   - **Amenities Word Cloud**: Visualization of top property features and facility keywords.

4. **🏢 Property Recommendation System (`pages/3_Recommended Appartments.py`)**
   - **Content-Based Similarity**: Computes similarity scores using weighted cosine similarity matrices over location features and amenity embeddings.
   - **Location Radius Search**: Filters apartments located within a specified radius (in kilometers) of a selected landmark or sector.

---
- **Machine Learning & Preprocessing**: Scikit-Learn, NumPy, Pandas, Joblib/Gzip
- **Data Visualization**: Plotly Express, Matplotlib, WordCloud
