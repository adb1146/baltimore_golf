import streamlit as st
import folium
from streamlit_folium import folium_static
from data.golf_courses import load_golf_courses

def show_map(filtered_df):
    st.header("Course Locations")
    
    # Get all courses data
    all_courses = load_golf_courses()
    
    # Create a map centered on Maryland with bounds restrictions
    m = folium.Map(
        location=[39.0458, -76.6413],
        zoom_start=10,  # Increased from 8 to 10 for closer initial view
        min_zoom=8,     # Increased from 7 to 8
        max_zoom=15,
        max_bounds=True,
        bounds=[[37.8, -79.5], [40.2, -74.5]]
    )
    
    # Determine which dataset to use for markers
    # If there are selected courses, use only those for markers
    if st.session_state.get('selected_courses', []):
        display_df = filtered_df[filtered_df['name'].isin(st.session_state['selected_courses'])]
    else:
        # If no courses are selected, show all courses
        display_df = all_courses
    
    # Add markers for each golf course
    for idx, row in display_df.iterrows():
        # Create a popup with more detailed information
        popup_html = f"""
            <div style='min-width: 200px'>
                <h4 style='margin-bottom: 10px'>{row['name']}</h4>
                <p><strong>Address:</strong><br>{row['address']}</p>
                <p><strong>Phone:</strong> {row['phone']}</p>
                <p><strong>Weekday Price:</strong> ${row['weekday_price']}</p>
                <p><strong>Weekend Price:</strong> ${row['weekend_price']}</p>
            </div>
        """
        
        # Add marker with enhanced popup and tooltip
        folium.Marker(
            [row['lat'], row['lon']],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=row['name'],
            icon=folium.Icon(color='green', icon='info-sign')
        ).add_to(m)
    
    # Fit bounds to show all markers if we have any courses to display
    if not display_df.empty:
        sw = display_df[['lat', 'lon']].min().values.tolist()
        ne = display_df[['lat', 'lon']].max().values.tolist()
        
        # Adjust padding based on the number of markers
        padding = 0.02 if len(display_df) > 1 else 0.01  # Reduced padding values
        
        # Calculate padded bounds
        padding_lat = (ne[0] - sw[0]) * padding
        padding_lon = (ne[1] - sw[1]) * padding
        sw = [sw[0] - padding_lat, sw[1] - padding_lon]
        ne = [ne[0] + padding_lat, ne[1] + padding_lon]
        
        # Ensure bounds stay within Maryland
        sw[0] = max(37.8, sw[0])
        sw[1] = max(-79.5, sw[1])
        ne[0] = min(40.2, ne[0])
        ne[1] = min(-74.5, ne[1])
        
        m.fit_bounds([sw, ne])
    
    # Display the map
    folium_static(m)
