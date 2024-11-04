import streamlit as st

def show_filters(df):
    st.sidebar.header("Filters")
    
    # Price range filter
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
    
    return df[mask]
