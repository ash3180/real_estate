import streamlit as st

st.set_page_config(
    page_title="Gurgaon Real Estate Analytics & Prediction App",
    page_icon="🏡",
    layout="wide"
)

st.title("🏡 Gurgaon Real Estate Analytics & Recommendation Portal")
st.markdown("### An End-to-End Machine Learning & Analytics Solution for Property Valuation")

st.markdown("---")

st.markdown("""
Welcome to the **Gurgaon Real Estate Web Platform**. This application offers comprehensive data analytics, 
machine learning-powered price valuation, and intelligent property recommendation engines tailored specifically for Gurgaon's residential market.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="📊 Sectors Analyzed", value="100+", delta="Coverage")
with col2:
    st.metric(label="💰 ML Prediction Model", value="Random Forest", delta="Log-Transformed")
with col3:
    st.metric(label="🏢 Recommender System", value="Content-Based", delta="Cosine Similarity")

st.markdown("---")

st.subheader("🛠️ Explore Platform Modules")

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.info("### 💰 Price Predictor")
    st.markdown("""
    Estimate property market values by specifying parameters such as:
    - **Property Type** (Flat / House)
    - **Sector & Location**
    - **Bedrooms, Bathrooms, Balconies**
    - **Area, Furnishing & Luxury Rating**
    """)
    st.page_link("pages/1_Price Predictor.py", label="Open Price Predictor ➡️", icon="💰")

with col_b:
    st.warning("### 📊 Real Estate Analytics")
    st.markdown("""
    Visual exploratory data analytics across Gurgaon:
    - **Geographic Sector Map** (Price/sq.ft vs Area)
    - **Price vs Built-Up Area** Scatter Trends
    - **BHK Distributions & Price Ranges**
    - **Amenities & Facilities Wordcloud**
    """)
    st.page_link("pages/2_Analysis App.py", label="Open Analytics Dashboard ➡️", icon="📊")

with col_c:
    st.success("### 🏢 Apartment Recommender")
    st.markdown("""
    Find the ideal property matches:
    - **Content-Based Similarity Engine**: Top 5 matching apartments based on features.
    - **Location Radius Search**: Discover apartment complexes within your target radius.
    """)
    st.page_link("pages/3_Recommended Appartments.py", label="Open Recommender Engine ➡️", icon="🏢")

st.markdown("---")

st.sidebar.success("👈 Select a module above to navigate.")
st.sidebar.markdown("---")
st.sidebar.markdown("**Tech Stack**: Python, Streamlit, Scikit-Learn, Pandas, Plotly, WordCloud")