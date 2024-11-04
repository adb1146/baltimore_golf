import streamlit as st
from data.database import get_course_details, update_course_details

def show_course_photos_and_holes(course_name):
    st.write("### Course Photos & Hole Details")
    
    # Get existing details
    details = get_course_details(course_name)
    
    # Admin section for adding/updating photos and descriptions
    st.markdown("#### 📸 Manage Course Photos & Hole Descriptions")
    
    # Photo URL input
    new_photo_url = st.text_input("Add Photo URL", key=f"photo_url_{course_name}")
    if st.button("Add Photo", key=f"add_photo_{course_name}"):
        current_photos = details.photos if details else []
        if new_photo_url and new_photo_url not in current_photos:
            updated_photos = current_photos + [new_photo_url]
            if update_course_details(course_name, photos=updated_photos):
                st.success("Photo added successfully!")
                st.rerun()
            else:
                st.error("Failed to add photo")
    
    # Hole description input
    st.markdown("#### Add/Update Hole Description")
    col1, col2 = st.columns([1, 2])
    with col1:
        hole_number = st.number_input("Hole Number", min_value=1, max_value=18, key=f"hole_num_{course_name}")
    with col2:
        hole_description = st.text_area("Hole Description", key=f"hole_desc_{course_name}")
    
    if st.button("Save Hole Description", key=f"save_hole_{course_name}"):
        current_descriptions = details.hole_descriptions if details else {}
        current_descriptions = current_descriptions or {}  # Handle None case
        current_descriptions[str(hole_number)] = hole_description
        if update_course_details(course_name, hole_descriptions=current_descriptions):
            st.success("Hole description saved successfully!")
            st.rerun()
        else:
            st.error("Failed to save hole description")
    
    st.markdown("---")
    
    # Display photos
    if details and details.photos:
        st.markdown("#### Course Photos")
        cols = st.columns(3)
        for i, photo_url in enumerate(details.photos):
            with cols[i % 3]:
                st.image(photo_url, use_column_width=True)
    else:
        st.info("No course photos available yet.")
    
    # Display hole descriptions
    if details and details.hole_descriptions:
        st.markdown("#### Hole-by-Hole Details")
        for hole_num in sorted(map(int, details.hole_descriptions.keys())):
            st.markdown(f"**⛳ Hole {hole_num}**")
            st.write(details.hole_descriptions[str(hole_num)])
            st.markdown("---")
    else:
        st.info("No hole descriptions available yet.")
