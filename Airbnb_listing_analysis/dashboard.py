import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import folium_static
import plotly.express as px

# Load dataset
data = pd.read_csv('datasets.csv', encoding_errors='ignore')

# Streamlit App Settings
st.set_page_config(page_title='Airbnb NYC Dashboard', layout='wide')
st.title('🏠 Airbnb Listings NYC - Data Analysis')
st.markdown("---")

# Sidebar Filters
st.sidebar.header('🔍 Filter Listings')
selected_neighborhood = st.sidebar.selectbox("Select Neighborhood", ['All'] + list(data['neighbourhood_group'].unique()))
price_range = st.sidebar.slider("Select Price Range", int(data['price'].min()), int(data['price'].max()), (50, 300))

# Filter data
filtered_data = data.copy()
if selected_neighborhood != 'All':
    filtered_data = filtered_data[filtered_data['neighbourhood_group'] == selected_neighborhood]
filtered_data = filtered_data[(filtered_data['price'] >= price_range[0]) & (filtered_data['price'] <= price_range[1])]

if filtered_data.empty:
    st.warning("⚠️ No listings available for the selected filters. Try adjusting the price range or neighborhood.")
else:
    # Data Overview
    st.subheader("📊 Data Overview")
    st.write(filtered_data.describe())
    st.markdown("---")

    # Price Distribution
    st.subheader("💰 Price Distribution")
    fig, ax = plt.subplots(figsize=(10,5))
    sns.histplot(filtered_data['price'], bins=50, kde=True, color='blue', ax=ax)
    st.pyplot(fig)
    st.markdown("---")

    # Correlation Heatmap
    st.subheader("📈 Correlation Matrix")
    numeric_cols = filtered_data.select_dtypes(include=[np.number])
    fig, ax = plt.subplots(figsize=(10,6))
    sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    st.pyplot(fig)
    st.markdown("---")

    # Bar Chart: Listings Per Neighborhood
    st.subheader("🏙️ Listings Per Neighborhood")
    neighborhood_counts = filtered_data['neighbourhood_group'].value_counts()
    fig = px.bar(neighborhood_counts, x=neighborhood_counts.index, y=neighborhood_counts.values, labels={'x': 'Neighborhood', 'y': 'Listings'}, color=neighborhood_counts.index)
    st.plotly_chart(fig)
    st.markdown("---")

    # Box Plot: Price by Room Type
    st.subheader("🛏️ Price Distribution by Room Type")
    fig = px.box(filtered_data, x='room_type', y='price', color='room_type', title="Price Variation by Room Type")
    st.plotly_chart(fig)
    st.markdown("---")

    # Availability Analysis
    st.subheader("📅 Availability of Listings")
    fig = px.histogram(filtered_data, x='availability_365', nbins=50, title='Availability Distribution')
    st.plotly_chart(fig)
    st.markdown("---")

    # Top Hosts
    st.subheader("👤 Top Hosts with Most Listings")
    top_hosts = filtered_data['host_name'].value_counts().head(10)
    fig = px.bar(top_hosts, x=top_hosts.index, y=top_hosts.values, labels={'x': 'Host Name', 'y': 'Number of Listings'}, color=top_hosts.index)
    st.plotly_chart(fig)
    st.markdown("---")

    # Room Type Distribution
    st.subheader("🏠 Room Type Distribution")
    fig = px.pie(filtered_data, names='room_type', title='Room Type Distribution')
    st.plotly_chart(fig)
    st.markdown("---")

    # Map Visualization
    st.subheader("🗺️ Airbnb Listings Map")
    map_nyc = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
    for _, row in filtered_data.sample(min(500, len(filtered_data))).iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=3,
            color='blue',
            fill=True,
            fill_color='blue'
        ).add_to(map_nyc)
    folium_static(map_nyc)
    
    st.markdown("### ✅ Data Analysis Completed!")
