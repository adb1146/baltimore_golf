import streamlit as st
from data.golf_courses import load_golf_courses
from components.filters import show_filters
from components.map_view import show_map
from components.course_details import show_course_details
from components.tee_times import show_tee_times
from components.reviews import show_course_reviews
from components.course_photos import show_course_photos_and_holes

# Page config must be the first Streamlit command
st.set_page_config(
    page_title="Baltimore Golf Courses",
    page_icon="⛳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS after page config
with open('.streamlit/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Title and introduction
st.markdown("""
    <div class='header-section'>
        <h1>⛳ Baltimore Area Golf Courses</h1>
        <p>
            Explore public golf courses in the Baltimore area. Find detailed information, 
            book tee times, and read reviews from other golfers.
        </p>
    </div>
""", unsafe_allow_html=True)

# Load data
df = load_golf_courses()

# Apply filters and get selected course from sidebar
filtered_df, selected_course = show_filters(df)

# Create main content area
main_container = st.container()

with main_container:
    # Show map at the top with proper spacing
    st.markdown("<div style='margin: 1rem 0;'>", unsafe_allow_html=True)
    show_map(filtered_df)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Show selected course details in tabs
    if selected_course:
        course_data = df[df['name'] == selected_course].iloc[0]
        
        # Create tabs with improved contrast
        st.markdown("<div style='margin: 2rem 0;'>", unsafe_allow_html=True)
        tabs = st.tabs([
            "📌 Course Info",
            "🕒 Tee Times",
            "⭐ Reviews",
            "📸 Photos & Holes"
        ])
        
        with tabs[0]:
            show_course_details(course_data)
            
        with tabs[1]:
            show_tee_times(selected_course)
            
        with tabs[2]:
            show_course_reviews(selected_course)
            
        with tabs[3]:
            show_course_photos_and_holes(selected_course)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='background-color: #ffffff; padding: 2rem; border-radius: 8px; text-align: center;'>
                <p style='color: #1a1a1a; font-size: 1.1rem;'>
                    Please select a course from the sidebar to view details.
                </p>
            </div>
        """, unsafe_allow_html=True)

# Footer with improved contrast
st.markdown("""
    <div class='footer-section'>
        <p>
            Data is for demonstration purposes only. Please contact individual courses 
            to verify current prices and availability.
        </p>
    </div>
""", unsafe_allow_html=True)
