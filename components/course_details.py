import streamlit as st
from components.reviews import show_course_reviews
from components.tee_times import show_tee_times
from components.course_photos import show_course_photos_and_holes

def show_course_details(df):
    st.markdown("""
        <div style='padding: 1rem 0;'>
            <h2 style='color: #2E7D32;'>Golf Courses</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Search functionality with improved styling
    st.markdown("""
        <style>
        .search-container {
            background-color: #f8f9fa;
            padding: 1rem;
            border-radius: 5px;
            margin-bottom: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
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
                    <p style='color: #666;'>{course['description']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Course details in columns
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                st.markdown("""
                    <div class='stat-item'>
                        <h4 style='color: #2E7D32;'>Location & Contact</h4>
                    </div>
                """, unsafe_allow_html=True)
                st.write("📍 **Address:**", course['address'])
                st.write("📞 **Phone:**", course['phone'])
            
            with col2:
                st.markdown("""
                    <div class='stat-item'>
                        <h4 style='color: #2E7D32;'>Course Details</h4>
                    </div>
                """, unsafe_allow_html=True)
                st.write("🏌️ **Holes:**", course['holes'])
                st.write("🎯 **Par:**", course['par'])
            
            with col3:
                st.markdown("""
                    <div class='stat-item'>
                        <h4 style='color: #2E7D32;'>Pricing</h4>
                    </div>
                """, unsafe_allow_html=True)
                st.write("💰 **Weekday:** $", course['weekday_price'])
                st.write("💰 **Weekend:** $", course['weekend_price'])
            
            # Amenities section
            st.markdown("""
                <div style='margin-top: 1rem;'>
                    <h4 style='color: #2E7D32;'>Amenities</h4>
                </div>
            """, unsafe_allow_html=True)
            amenities_list = course['amenities'].split(', ')
            cols = st.columns(len(amenities_list))
            for i, amenity in enumerate(amenities_list):
                with cols[i]:
                    st.markdown(f"""
                        <div style='background-color: #f8f9fa; padding: 0.5rem; 
                        border-radius: 5px; text-align: center;'>
                            {amenity}
                        </div>
                    """, unsafe_allow_html=True)
            
            # Add photos and hole descriptions section
            st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
            show_course_photos_and_holes(course['name'])
            
            # Add tee times section
            st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
            show_tee_times(course['name'])
            
            # Add reviews section
            st.markdown("<hr style='margin: 2rem 0;'>", unsafe_allow_html=True)
            show_course_reviews(course['name'])
