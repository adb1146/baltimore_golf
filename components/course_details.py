import streamlit as st
from components.reviews import show_course_reviews
from components.tee_times import show_tee_times
from components.course_photos import show_course_photos_and_holes

def show_course_details(df):
    st.markdown("""
        <div class='header-section'>
            <h2 style='color: #2E7D32; margin-bottom: 1rem;'>Golf Courses</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Search functionality with improved styling
    with st.container():
        col1, col2 = st.columns([2, 1])
        with col1:
            search_term = st.text_input("🔍 Search courses", "", 
                help="Search by course name or description")
        with col2:
            sort_by = st.selectbox(
                "Sort by",
                ["Name", "Weekday Price", "Weekend Price"],
                help="Choose how to sort the courses"
            )
    
    if search_term:
        df = df[df['name'].str.contains(search_term, case=False) |
                df['description'].str.contains(search_term, case=False)]
    
    if sort_by == "Name":
        df = df.sort_values('name')
    elif sort_by == "Weekday Price":
        df = df.sort_values('weekday_price')
    else:
        df = df.sort_values('weekend_price')
    
    # Display course details with enhanced styling
    for _, course in df.iterrows():
        with st.expander(f"🏌️ {course['name']}"):
            # Course header
            st.markdown(f"""
                <div class='course-header'>
                    <h3 style='color: #2E7D32; margin-bottom: 1rem;'>{course['name']}</h3>
                    <p style='color: #333;'>{course['description']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Course details in columns
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                st.markdown("""
                    <div class='stat-item'>
                        <h4 style='color: #2E7D32; margin-bottom: 1rem;'>Location & Contact</h4>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                    <div style='color: #333;'>
                        <p>📍 <strong>Address:</strong> {course['address']}</p>
                        <p>📞 <strong>Phone:</strong> {course['phone']}</p>
                    </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                    <div class='stat-item'>
                        <h4 style='color: #2E7D32; margin-bottom: 1rem;'>Course Details</h4>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                    <div style='color: #333;'>
                        <p>🏌️ <strong>Holes:</strong> {course['holes']}</p>
                        <p>🎯 <strong>Par:</strong> {course['par']}</p>
                    </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                    <div class='stat-item'>
                        <h4 style='color: #2E7D32; margin-bottom: 1rem;'>Pricing</h4>
                    </div>
                """, unsafe_allow_html=True)
                st.markdown(f"""
                    <div style='color: #333;'>
                        <p>💰 <strong>Weekday:</strong> ${course['weekday_price']}</p>
                        <p>💰 <strong>Weekend:</strong> ${course['weekend_price']}</p>
                    </div>
                """, unsafe_allow_html=True)
            
            # Amenities section
            st.markdown("""
                <div style='margin-top: 2rem; margin-bottom: 1rem;'>
                    <h4 style='color: #2E7D32;'>Amenities</h4>
                </div>
            """, unsafe_allow_html=True)
            
            amenities_list = course['amenities'].split(', ')
            cols = st.columns(len(amenities_list))
            for i, amenity in enumerate(amenities_list):
                with cols[i]:
                    st.markdown(f"""
                        <div class='amenity-tag'>
                            {amenity}
                        </div>
                    """, unsafe_allow_html=True)
            
            # Additional sections with proper spacing and styling
            st.markdown("<hr style='margin: 2rem 0; border-color: #eee;'>", unsafe_allow_html=True)
            show_course_photos_and_holes(course['name'])
            
            st.markdown("<hr style='margin: 2rem 0; border-color: #eee;'>", unsafe_allow_html=True)
            show_tee_times(course['name'])
            
            st.markdown("<hr style='margin: 2rem 0; border-color: #eee;'>", unsafe_allow_html=True)
            show_course_reviews(course['name'])
