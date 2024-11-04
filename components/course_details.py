import streamlit as st
from components.reviews import show_course_reviews
from components.tee_times import show_tee_times
from components.course_photos import show_course_photos_and_holes

def show_course_details(df):
    st.header("Golf Courses")
    
    # Search functionality
    search_term = st.text_input("Search courses", "")
    if search_term:
        df = df[df['name'].str.contains(search_term, case=False) |
                df['description'].str.contains(search_term, case=False)]
    
    # Sorting options
    sort_by = st.selectbox(
        "Sort by",
        ["Name", "Weekday Price", "Weekend Price"]
    )
    
    if sort_by == "Name":
        df = df.sort_values('name')
    elif sort_by == "Weekday Price":
        df = df.sort_values('weekday_price')
    else:
        df = df.sort_values('weekend_price')
    
    # Display course details
    for _, course in df.iterrows():
        with st.expander(course['name']):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Address:**", course['address'])
                st.write("**Phone:**", course['phone'])
                st.write("**Description:**", course['description'])
            
            with col2:
                st.write("**Holes:**", course['holes'])
                st.write("**Par:**", course['par'])
                st.write("**Weekday Price:** $", course['weekday_price'])
                st.write("**Weekend Price:** $", course['weekend_price'])
                st.write("**Amenities:**", course['amenities'])
            
            # Add photos and hole descriptions section
            st.markdown("---")
            show_course_photos_and_holes(course['name'])
            
            # Add tee times section
            st.markdown("---")
            show_tee_times(course['name'])
            
            # Add reviews section
            st.markdown("---")
            show_course_reviews(course['name'])
