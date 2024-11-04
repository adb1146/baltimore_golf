import streamlit as st
from data.golf_courses import load_golf_courses
from components.filters import show_filters
from components.map_view import show_map
from components.course_details import show_course_details

# Page config
st.set_page_config(
    page_title="Baltimore Golf Courses",
    page_icon="⛳",
    layout="wide"
)

# Title and introduction
st.title("⛳ Baltimore Area Golf Courses")
st.markdown("""
    Explore public golf courses in the Baltimore area. Use the sidebar filters to find 
    courses that match your preferences, and click on course names for detailed information.
""")

# Load data
df = load_golf_courses()

# Apply filters from sidebar
filtered_df = show_filters(df)

# Show map
show_map(filtered_df)

# Show course details
show_course_details(filtered_df)

# Footer
st.markdown("""
    ---
    Data is for demonstration purposes only. Please contact individual courses to verify 
    current prices and availability.
""")
