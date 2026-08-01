import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title='Recommended Apartments | Gurgaon', page_icon='🏢', layout='wide')

st.title("🏢 Property Recommendation & Radius Search")
st.markdown("Find similar apartments based on property attributes or search for complexes within a specific radius of key locations.")

@st.cache_data
def load_recommendation_data():
    with open('datasets/location_distance.pkl', 'rb') as f:
        location_df = pickle.load(f)
    with open('datasets/cosine_sim1.pkl', 'rb') as f:
        cosine_sim1 = pickle.load(f)
    with open('datasets/cosine_sim2.pkl', 'rb') as f:
        cosine_sim2 = pickle.load(f)
    with open('datasets/cosine_sim3.pkl', 'rb') as f:
        cosine_sim3 = pickle.load(f)
    return location_df, cosine_sim1, cosine_sim2, cosine_sim3

location_df, cosine_sim1, cosine_sim2, cosine_sim3 = load_recommendation_data()

def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]
    top_properties = location_df.index[top_indices].tolist()

    recommendations_df = pd.DataFrame({
        'Property Name': top_properties,
        'Similarity Score': [round(s, 4) for s in top_scores]
    })
    return recommendations_df

tab1, tab2 = st.tabs(["🎯 Similar Apartments Recommender", "📍 Location & Radius Search"])

with tab1:
    st.subheader("Content-Based Apartment Recommendation")
    st.markdown("Select your preferred apartment complex to discover the top 5 most similar projects in Gurgaon.")
    
    selected_apartment = st.selectbox('Select an Apartment Complex', sorted(location_df.index.to_list()))
    
    if st.button('✨ Find Similar Apartments', type="primary"):
        with st.spinner("Finding best matching properties..."):
            recommendation_df = recommend_properties_with_scores(selected_apartment)
        
        st.success(f"Top 5 Recommendations Similar to **{selected_apartment}**:")
        st.dataframe(recommendation_df, use_container_width=True)

with tab2:
    st.subheader("Nearby Apartments by Location & Radius")
    st.markdown("Search for apartment complexes within your target radius (in Kilometers) of a selected landmark or sector.")
    
    col1, col2 = st.columns(2)
    with col1:
        selected_location = st.selectbox('Select Benchmark Location / Landmark', sorted(location_df.columns.to_list()))
    with col2:
        radius = st.number_input('Search Radius (in Kms)', min_value=1.0, max_value=50.0, value=5.0, step=1.0)
        
    if st.button('🔍 Search Nearby Properties', use_container_width=True):
        result_ser = location_df[location_df[selected_location] <= radius * 1000][selected_location].sort_values()
        
        if len(result_ser) == 0:
            st.warning("No apartments found within the selected radius.")
        else:
            nearby_df = pd.DataFrame({
                'Apartment Complex': result_ser.index,
                'Distance (Km)': (result_ser.values / 1000.0).round(2)
            })
            st.success(f"Found **{len(nearby_df)}** apartments within **{radius} km** of **{selected_location}**:")
            st.dataframe(nearby_df, use_container_width=True)
