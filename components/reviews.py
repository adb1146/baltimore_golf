import streamlit as st
from data.database import add_review, get_course_reviews, get_course_average_rating

def show_course_reviews(course_name):
    st.write("### Reviews")
    
    # Display average rating
    avg_rating = get_course_average_rating(course_name)
    if avg_rating:
        st.write(f"Average Rating: ⭐ {avg_rating:.1f}/5.0")
    else:
        st.write("No ratings yet")
    
    # Add review form
    st.write("### Add Your Review")
    with st.form(key=f"review_form_{course_name}"):
        user_name = st.text_input("Your Name")
        rating = st.slider("Rating", min_value=1.0, max_value=5.0, value=5.0, step=0.5)
        comment = st.text_area("Review Comment")
        submit_button = st.form_submit_button(label="Submit Review")
        
        if submit_button:
            if user_name and comment:
                if add_review(course_name, user_name, rating, comment):
                    st.success("Review submitted successfully!")
                    st.experimental_rerun()
                else:
                    st.error("Failed to submit review. Please try again.")
            else:
                st.warning("Please fill in all fields")
    
    # Display existing reviews
    st.write("### User Reviews")
    reviews = get_course_reviews(course_name)
    if reviews:
        for review in reviews:
            with st.expander(f"{review.user_name} - ⭐ {review.rating}"):
                st.write(review.comment)
                st.caption(f"Posted on {review.created_at.strftime('%Y-%m-%d %H:%M')}")
    else:
        st.info("No reviews yet. Be the first to review!")
