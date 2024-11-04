import streamlit as st

def show_course_details(course):
    """Display details for a single selected course"""
    # Course header
    st.markdown(f"""
        <div class='course-header'>
            <h3>{course['name']}</h3>
            <p>{course['description']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Course details in columns
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("""
            <div class='stat-item'>
                <h4>Location & Contact</h4>
                <p>📍 <strong>Address:</strong></p>
                <p style='color: #1a1a1a; margin-left: 1.5rem;'>{address}</p>
                <p>📞 <strong>Phone:</strong></p>
                <p style='color: #1a1a1a; margin-left: 1.5rem;'>{phone}</p>
            </div>
        """.format(
            address=course['address'],
            phone=course['phone']
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class='stat-item'>
                <h4>Course Details</h4>
                <p>🏌️ <strong>Holes:</strong> {holes}</p>
                <p>🎯 <strong>Par:</strong> {par}</p>
            </div>
        """.format(
            holes=course['holes'],
            par=course['par']
        ), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class='stat-item'>
                <h4>Pricing</h4>
                <p>💰 <strong>Weekday:</strong> ${weekday}</p>
                <p>💰 <strong>Weekend:</strong> ${weekend}</p>
            </div>
        """.format(
            weekday=course['weekday_price'],
            weekend=course['weekend_price']
        ), unsafe_allow_html=True)
    
    # Amenities section
    st.markdown("<h4 style='color: #1a1a1a; margin: 2rem 0 1rem 0;'>Amenities</h4>", unsafe_allow_html=True)
    
    amenities_list = course['amenities'].split(', ')
    cols = st.columns(len(amenities_list))
    for i, amenity in enumerate(amenities_list):
        with cols[i]:
            st.markdown(f"""
                <div class='amenity-tag'>
                    {amenity}
                </div>
            """, unsafe_allow_html=True)
