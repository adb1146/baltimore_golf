import streamlit as st
import folium
from streamlit_folium import folium_static

def show_map(df):
    st.header("Course Locations")
    
    # Create a map centered on Baltimore
    m = folium.Map(
        location=[39.2904, -76.6122],
        zoom_start=11
    )
    
    # Add markers for each golf course
    for idx, row in df.iterrows():
        folium.Marker(
            [row['lat'], row['lon']],
            popup=f"""
                <b>{row['name']}</b><br>
                {row['address']}<br>
                Phone: {row['phone']}
            """,
            tooltip=row['name']
        ).add_to(m)
    
    # Display the map
    folium_static(m)
