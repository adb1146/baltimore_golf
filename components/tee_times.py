import streamlit as st
from datetime import datetime, date
from data.database import generate_tee_times, get_available_tee_times, book_tee_time

def show_tee_times(course_name):
    st.write("### Tee Times")
    
    # Date selector
    selected_date = st.date_input(
        "Select Date",
        min_value=date.today(),
        value=date.today()
    )
    
    # Generate tee times button
    if st.button("Generate Tee Times"):
        if generate_tee_times(course_name, selected_date):
            st.success("Tee times generated successfully!")
        else:
            st.error("Failed to generate tee times")
    
    # Display available tee times
    tee_times = get_available_tee_times(course_name, selected_date)
    
    if tee_times:
        st.write("Available Tee Times:")
        
        # Create columns for better organization
        cols = st.columns(4)
        for i, tee_time in enumerate(tee_times):
            col = cols[i % 4]
            with col:
                time_str = tee_time.tee_time.strftime("%I:%M %p")
                if tee_time.available:
                    # Create a unique key for each booking form
                    with st.form(key=f"booking_form_{tee_time.id}"):
                        st.write(f"🕒 {time_str}")
                        user_name = st.text_input("Your Name", key=f"name_{tee_time.id}")
                        book_button = st.form_submit_button("Book")
                        
                        if book_button:
                            if user_name:
                                if book_tee_time(tee_time.id, user_name):
                                    st.success("Tee time booked successfully!")
                                    st.experimental_rerun()
                                else:
                                    st.error("Failed to book tee time")
                            else:
                                st.warning("Please enter your name")
                else:
                    st.write(f"🕒 {time_str} (Booked)")
    else:
        st.info("No tee times available for the selected date. Click 'Generate Tee Times' to create new time slots.")
