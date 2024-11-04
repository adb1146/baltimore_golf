import streamlit as st
import openai
import os
from data.golf_courses import load_golf_courses

def get_all_courses_info():
    """Get detailed information about all courses"""
    df = load_golf_courses()
    courses_info = []
    
    for _, course in df.iterrows():
        courses_info.append({
            'name': course['name'],
            'address': course['address'],
            'phone': course['phone'],
            'holes': course['holes'],
            'par': course['par'],
            'weekday_price': course['weekday_price'],
            'weekend_price': course['weekend_price'],
            'amenities': course['amenities'],
            'description': course['description']
        })
    return courses_info

def get_ai_response(messages):
    """Get response from OpenAI API"""
    try:
        client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=250
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"I apologize, but I'm having trouble processing your request. Please try again later."

def show_chat_interface():
    st.write("### 🤖 Golf Course Assistant")
    st.write("Ask about courses, get recommendations, or inquire about specific features!")
    
    # Initialize chat history in session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
        
    # Get all courses information
    courses_info = get_all_courses_info()
    
    # Create a formatted string of course information
    courses_data = "\n\n".join([
        f"Course: {course['name']}\n"
        f"Location: {course['address']}\n"
        f"Pricing: Weekday ${course['weekday_price']}, Weekend ${course['weekend_price']}\n"
        f"Details: {course['holes']} holes, Par {course['par']}\n"
        f"Amenities: {course['amenities']}\n"
        f"Description: {course['description']}"
        for course in courses_info
    ])
    
    # System message with all courses information
    system_message = f"""You are a helpful golf course assistant for Baltimore area golf courses.
    You have access to information about all courses and can help users find the right course for their needs.
    Here are all the available courses and their details:
    
    {courses_data}
    
    Help users find suitable courses based on their preferences such as:
    - Location/area
    - Price range
    - Amenities
    - Difficulty level
    - Special features
    
    Provide recommendations and then guide users to select courses using the sidebar."""
    
    # Chat container with custom styling
    chat_container = st.container()
    
    with chat_container:
        # Display chat history with improved contrast
        for message in st.session_state.chat_history:
            role = message["role"]
            content = message["content"]
            
            if role == "user":
                st.markdown("""
                    <div style='background-color: #e9ecef; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;'>
                        <strong style='color: #1a1a1a;'>You:</strong><br>
                        <span style='color: #1a1a1a;'>{content}</span>
                    </div>
                """.format(content=content), unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div style='background-color: #ffffff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border: 1px solid #dee2e6;'>
                        <strong style='color: #1a1a1a;'>Assistant:</strong><br>
                        <span style='color: #1a1a1a;'>{content}</span>
                    </div>
                """.format(content=content), unsafe_allow_html=True)
    
    # Chat input form with submit and clear buttons
    with st.form(key='chat_form', clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        
        with col1:
            user_input = st.text_input(
                "Type your question here:",
                placeholder="e.g., What courses have driving ranges?",
                key="chat_input"
            )
        
        with col2:
            submit_button = st.form_submit_button("Send")
            clear_button = st.button("Clear Chat")
    
        if submit_button and user_input:
            # Add user message to history
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            
            # Prepare messages for API
            messages = [
                {"role": "system", "content": system_message}
            ]
            # Add relevant history for context but limit to last few messages
            messages.extend(st.session_state.chat_history[-5:])
            
            # Get AI response
            ai_response = get_ai_response(messages)
            
            # Add AI response to history
            st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
    
    # Handle clear button
    if clear_button:
        st.session_state.chat_history = []