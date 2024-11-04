import streamlit as st

def show_filters(df):
    st.sidebar.header("Course Selection & Filters")
    
    # Multiple course selection
    selected_courses = st.sidebar.multiselect(
        "Select Courses",
        options=df['name'].tolist(),
        default=st.session_state.get('selected_courses', []),
        help="Choose one or more golf courses to view details"
    )
    
    # Reset button for filters
    if st.sidebar.button("Reset All Filters", key="reset_filters"):
        # Clear all selections and reset to defaults
        st.session_state['selected_courses'] = []
        st.session_state['sort_by'] = "Name"
        st.session_state['price_range'] = (
            int(df['weekday_price'].min()),
            int(df['weekday_price'].max())
        )
        st.session_state['selected_amenities'] = []
        # Force a rerun to update the UI
        st.rerun()
    
    # Sort options
    sort_by = st.sidebar.selectbox(
        "Sort Course List By",
        ["Name", "Weekday Price", "Weekend Price"],
        help="Choose how to sort the courses",
        key="sort_by"
    )
    
    # Price range filter
    st.sidebar.subheader("Filters")
    price_range = st.sidebar.slider(
        "Weekday Price Range",
        min_value=int(df['weekday_price'].min()),
        max_value=int(df['weekday_price'].max()),
        value=(
            int(df['weekday_price'].min()),
            int(df['weekday_price'].max())
        ),
        key="price_range"
    )
    
    # Amenities filter
    all_amenities = set()
    for amenities in df['amenities']:
        all_amenities.update([a.strip() for a in amenities.split(',')])
    selected_amenities = st.sidebar.multiselect(
        "Select Amenities",
        sorted(list(all_amenities)),
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
        # Update session state with selected courses
        st.session_state['selected_courses'] = selected_courses
    
    # Apply sorting
    if sort_by == "Name":
        filtered_df = filtered_df.sort_values('name')
    elif sort_by == "Weekday Price":
        filtered_df = filtered_df.sort_values('weekday_price')
    else:
        filtered_df = filtered_df.sort_values('weekend_price')
    
    # Return the filtered dataframe and all selected courses
    return filtered_df, selected_courses
