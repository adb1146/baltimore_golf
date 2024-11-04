import streamlit as st
from data.golf_courses import load_golf_courses
from components.filters import show_filters
from components.map_view import show_map
from components.course_details import show_course_details

# Load custom CSS
with open('.streamlit/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Page config with custom theme
st.set_page_config(
    page_title="Baltimore Golf Courses",
    page_icon="⛳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for page layout
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True)

# Title and introduction with enhanced styling
st.markdown("""
    <div style='text-align: center; padding: 2rem 0;'>
        <h1 style='color: #2E7D32;'>⛳ Baltimore Area Golf Courses</h1>
        <p style='font-size: 1.2rem; color: #666;'>
            Explore public golf courses in the Baltimore area. Use the sidebar filters to find 
            courses that match your preferences, and click on course names for detailed information.
        </p>
    </div>
""", unsafe_allow_html=True)

# Load data
df = load_golf_courses()

# Create three main columns for layout
left_col, center_col = st.columns([1, 3])

with left_col:
    # Apply filters from sidebar
    filtered_df = show_filters(df)

with center_col:
    # Show map
    show_map(filtered_df)
    
    # Show course details
    show_course_details(filtered_df)

# Footer with enhanced styling
st.markdown("""
    <div style='text-align: center; padding: 2rem 0; margin-top: 3rem; border-top: 1px solid #eee;'>
        <p style='color: #666; font-size: 0.9rem;'>
            Data is for demonstration purposes only. Please contact individual courses to verify 
            current prices and availability.
        </p>
    </div>
""", unsafe_allow_html=True)
