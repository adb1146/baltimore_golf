import streamlit as st

def show_course_details(course):
    """Display details for a single selected course"""
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
                <h4 style='color: #2E7D32; margin-bottom: 0.5rem;'>Location & Contact</h4>
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
                <h4 style='color: #2E7D32; margin-bottom: 0.5rem;'>Course Details</h4>
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
                <h4 style='color: #2E7D32; margin-bottom: 0.5rem;'>Pricing</h4>
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
        <div style='margin-top: 1rem;'>
            <h4 style='color: #2E7D32; margin-bottom: 0.5rem;'>Amenities</h4>
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
