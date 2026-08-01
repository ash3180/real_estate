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

## 📁 Repository Structure

```
gurgaonrealestate/
├── Home.py                       # Main Streamlit App entrypoint
├── requirements.txt              # Required Python dependencies
├── .gitignore                    # Git ignore configuration
├── README.md                     # Project documentation
├── df.pkl                        # Processed dataframe pickle
├── pipeline.pkl.gz               # Compressed ML model pipeline (~31 MB)
├── pages/                        # Multi-page Streamlit routes
│   ├── 1_Price Predictor.py      # Price prediction interface
│   ├── 2_Analysis App.py         # Data analytics dashboard
│   └── 3_Recommended Appartments.py # Recommender engine & radius search
└── datasets/                     # Processed datasets & matrices
    ├── data_viz1.csv             # Analytics dataset
    ├── location_distance.pkl     # Pairwise distance matrix
    ├── cosine_sim1.pkl           # Cosine similarity matrix 1
    ├── cosine_sim2.pkl           # Cosine similarity matrix 2
    ├── cosine_sim3.pkl           # Cosine similarity matrix 3
    ├── feature_text.pkl          # Amenity text corpus
```

---

## 🚀 Local Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/gurgaonrealestate.git
cd gurgaonrealestate
```

### 2. Create a Virtual Environment
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run Home.py
```
Open your browser at `http://localhost:8501`.

---

## ☁️ Deploying to Streamlit Community Cloud

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Prepare Gurgaon Real Estate app for Streamlit deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Community Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io/).
   - Sign in with your GitHub account.
   - Click **New app**.
   - Select your repository (`YOUR_USERNAME/gurgaonrealestate`).
   - Set **Main file path** to: `Home.py`.
   - Click **Deploy!**

---

## 🛠️ Tech Stack & Libraries

- **Framework**: Streamlit
- **Machine Learning & Preprocessing**: Scikit-Learn, NumPy, Pandas, Joblib/Gzip
- **Data Visualization**: Plotly Express, Matplotlib, WordCloud
