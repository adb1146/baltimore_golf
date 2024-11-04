import streamlit as st

def show_filters(df):
    st.sidebar.header("Course Selection & Filters")
    
    # Course selection
    selected_course = st.sidebar.selectbox(
        "Select Course",
        options=df['name'].tolist(),
        help="Choose a golf course to view details"
    )
    
    # Sort options
    sort_by = st.sidebar.selectbox(
        "Sort Course List By",
        ["Name", "Weekday Price", "Weekend Price"],
        help="Choose how to sort the courses"
    )
    
    # Price range filter
    st.sidebar.subheader("Filters")
    price_range = st.sidebar.slider(
        "Weekday Price Range",
        min_value=int(df['weekday_price'].min()),
        max_value=int(df['weekday_price'].max()),
        value=(int(df['weekday_price'].min()), int(df['weekday_price'].max()))
    )
    
    # Amenities filter
    all_amenities = set()
    for amenities in df['amenities']:
        all_amenities.update([a.strip() for a in amenities.split(',')])
    selected_amenities = st.sidebar.multiselect(
        "Select Amenities",
        sorted(list(all_amenities))
    )
    
    # Apply filters
    mask = (df['weekday_price'].between(price_range[0], price_range[1]))
    if selected_amenities:
        mask = mask & df['amenities'].apply(
            lambda x: any(amenity in x for amenity in selected_amenities)
        )
    
    filtered_df = df[mask]
    
    # Apply sorting
    if sort_by == "Name":
        filtered_df = filtered_df.sort_values('name')
    elif sort_by == "Weekday Price":
        filtered_df = filtered_df.sort_values('weekday_price')
    else:
        filtered_df = filtered_df.sort_values('weekend_price')
    
    return filtered_df, selected_course
