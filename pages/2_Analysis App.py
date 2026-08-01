import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import matplotlib.pyplot as plt

try:
    from wordcloud import WordCloud
    HAS_WORDCLOUD = True
except ImportError:
    HAS_WORDCLOUD = False

st.set_page_config(page_title="Real Estate Analytics | Gurgaon", page_icon="📊", layout="wide")

st.title("📊 Real Estate Analytics Dashboard")
st.markdown("Explore spatial price distributions, amenities wordcloud, and pricing trends across Gurgaon properties.")

@st.cache_data
def load_viz_data():
    df = pd.read_csv('datasets/data_viz1.csv')
    with open('datasets/feature_text.pkl', 'rb') as f:
        feature_text = pickle.load(f)
    return df, feature_text

new_df, feature_text = load_viz_data()

tab1, tab2, tab3 = st.tabs(["🗺️ Geographic Map", "📈 Market & Area Trends", "☁️ Amenities Wordcloud"])

with tab1:
    st.subheader("Sector Price Distribution Across Gurgaon")
    st.caption("Map size represents average built-up area; color intensity represents average price per sq. ft.")
    group_df = new_df.groupby('sector')[['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']].mean()
    
    fig_map = px.scatter_mapbox(
        group_df,
        lat="latitude",
        lon="longitude",
        color="price_per_sqft",
        size='built_up_area',
        color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=10,
        mapbox_style="open-street-map",
        height=650,
        hover_name=group_df.index
    )
    st.plotly_chart(fig_map, use_container_width=True)

with tab2:
    st.subheader("Area vs Price Analysis")
    property_type = st.selectbox("Select Property Type", ['flat', 'house'], key='prop_type_select')
    
    filtered_df = new_df[new_df['property_type'] == property_type]
    fig_scatter = px.scatter(
        filtered_df,
        x="built_up_area",
        y="price",
        color="bedRoom",
        title=f"Built-Up Area vs Price ({property_type.capitalize()})",
        labels={"built_up_area": "Built-Up Area (sq. ft.)", "price": "Price (in Cr)", "bedRoom": "Bedrooms"}
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("BHK Distribution")
        sector_options = ['overall'] + sorted(new_df['sector'].unique().tolist())
        selected_sector = st.selectbox("Select Sector", sector_options)
        
        if selected_sector == 'overall':
            pie_data = new_df
        else:
            pie_data = new_df[new_df['sector'] == selected_sector]
            
        fig_pie = px.pie(pie_data, names='bedRoom', title=f"Bedroom Breakdown ({selected_sector.capitalize()})")
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col2:
        st.subheader("BHK Price Comparison")
        fig_box = px.box(
            new_df[new_df['bedRoom'] <= 4],
            x='bedRoom',
            y='price',
            title='Price Range by Bedroom Count (≤ 4 BHK)',
            labels={"bedRoom": "Bedrooms", "price": "Price (in Cr)"}
        )
        st.plotly_chart(fig_box, use_container_width=True)

with tab3:
    st.subheader("Popular Property Facilities and Amenities")
    st.caption("Word cloud generated from property feature descriptions and amenity tags.")
    
    if HAS_WORDCLOUD:
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color='white',
            stopwords=set(['s']),
            min_font_size=10
        ).generate(feature_text)

        fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
        ax_wc.imshow(wordcloud, interpolation='bilinear')
        ax_wc.axis("off")
        fig_wc.tight_layout(pad=0)
        
        st.pyplot(fig_wc)
    else:
        st.info("ℹ️ `wordcloud` library is not installed in the local environment.")
        st.code("pip install wordcloud", language="bash")
        st.markdown("**Sample High-Frequency Amenities:**")
        st.write(feature_text[:300] + "...")