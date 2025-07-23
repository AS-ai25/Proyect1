import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data
data = {
    'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney'],
    'Temperature (°C)': [30, 22, 25, 33, 28],
    'Latitude': [40.7128, 51.5074, 48.8566, 35.6895, -33.8688],
    'Longitude': [-74.0060, -0.1278, 2.3522, 139.6917, 151.2093]
}
df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.title("🌍 Select temperature range")
temp_range = st.sidebar.slider("Temperature (°C)", 0, 40, (20, 35))

# Filter data
filtered_df = df[df['Temperature (°C)'].between(*temp_range)]

# Title
st.title("🌡️ World Cities Temperature Dashboard")

# Show data
st.subheader("📊 Filtered Cities")
st.dataframe(filtered_df)

# Plot
fig = px.bar(filtered_df, x='City', y='Temperature (°C)', color='Temperature (°C)',
             color_continuous_scale='viridis')
st.plotly_chart(fig)

# Map
st.subheader("🗺️ City Map")
st.map(filtered_df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'}))
