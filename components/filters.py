import streamlit as st

def show_filters(df):
    st.sidebar.header("Course Selection & Filters")
    
    # Get current selected courses from session state
    selected_courses = st.session_state.get('selected_courses', [])
    
    # Get available courses (excluding selected ones)
    available_courses = [c for c in df['name'].tolist() if c not in selected_courses]

    # Update multiselect to only show available courses
    selected_new_courses = st.sidebar.multiselect(
        "Select Courses",
        options=available_courses,
        default=[],
        key='course_selector',
        help="Choose one or more golf courses to view details"
    )

    # Add newly selected courses to the list
    if selected_new_courses:
        selected_courses.extend(selected_new_courses)
        st.session_state['selected_courses'] = selected_courses
        st.rerun()
    
    # Display selected courses with remove buttons
    if selected_courses:
        st.sidebar.markdown("### Selected Courses:")
        for course in selected_courses:
            col1, col2 = st.sidebar.columns([4, 1])
            with col1:
                st.markdown(f"- {course}")
            with col2:
                if st.button("×", key=f"remove_{course}", 
                    help=f"Remove {course}", 
                    type="secondary",
                    use_container_width=False):
                    selected_courses.remove(course)
                    st.session_state['selected_courses'] = selected_courses
                    st.rerun()
    else:
        st.sidebar.info("No courses selected")
    
    # Reset button for filters
    if st.sidebar.button("Reset All Filters", key="reset_filters"):
        # Clear all selections and reset to defaults
        st.session_state['selected_courses'] = []
        st.session_state['sort_by'] = "Name"
        default_price_range = (
            int(df['weekday_price'].min()),
            int(df['weekday_price'].max())
        )
        st.session_state['price_range'] = default_price_range
        st.session_state['selected_amenities'] = []
        st.rerun()
    
    # Sort options
    sort_by = st.sidebar.selectbox(
        "Sort Course List By",
        ["Name", "Weekday Price", "Weekend Price"],
        help="Choose how to sort the courses",
        key="sort_by"
    )
    
    # Price range filter with fixed session state handling
    st.sidebar.subheader("Filters")
    default_price_range = (
        int(df['weekday_price'].min()),
        int(df['weekday_price'].max())
    )
    price_range = st.sidebar.slider(
        "Weekday Price Range",
        min_value=int(df['weekday_price'].min()),
        max_value=int(df['weekday_price'].max()),
        value=st.session_state.get('price_range', default_price_range)
    )
    st.session_state['price_range'] = price_range
    
    # Amenities filter
    all_amenities = set()
    for amenities in df['amenities']:
        all_amenities.update([a.strip() for a in amenities.split(',')])
    selected_amenities = st.sidebar.multiselect(
        "Select Amenities",
        sorted(list(all_amenities)),
        default=st.session_state.get('selected_amenities', []),
        key="selected_amenities"
    )
    
    # Apply filters
    mask = (df['weekday_price'].between(price_range[0], price_range[1]))
    if selected_amenities:
        mask = mask & df['amenities'].apply(
            lambda x: any(amenity in x for amenity in selected_amenities)
        )
    
    filtered_df = df[mask]
    
    # Further filter by selected courses if any are selected
    if selected_courses:
        filtered_df = filtered_df[filtered_df['name'].isin(selected_courses)]
    
    # Apply sorting
    if sort_by == "Name":
        filtered_df = filtered_df.sort_values('name')
    elif sort_by == "Weekday Price":
        filtered_df = filtered_df.sort_values('weekday_price')
    else:
        filtered_df = filtered_df.sort_values('weekend_price')
    
    return filtered_df, selected_courses
