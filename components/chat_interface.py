import streamlit as st
import openai
import os
from data.golf_courses import load_golf_courses

def get_course_info(course_name):
    """Get detailed information about a specific course"""
    df = load_golf_courses()
    course = df[df['name'] == course_name].iloc[0]
    return {
        'name': course['name'],
        'address': course['address'],
        'phone': course['phone'],
        'holes': course['holes'],
        'par': course['par'],
        'weekday_price': course['weekday_price'],
        'weekend_price': course['weekend_price'],
        'amenities': course['amenities'],
        'description': course['description']
    }

def get_ai_response(messages):
    """Get response from OpenAI API"""
    try:
        client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"I apologize, but I'm having trouble processing your request. Please try again later."

def show_chat_interface(course_name):
    st.write("### Golf Course Assistant")
    st.write("Ask questions about the course, tee times, amenities, or anything else!")
    
    # Initialize chat history in session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
        
    # Get course information
    course_info = get_course_info(course_name)
    
    # System message with course information
    system_message = f"""You are a helpful golf course assistant for {course_name}. 
    Here are the course details:
    - Address: {course_info['address']}
    - Phone: {course_info['phone']}
    - Holes: {course_info['holes']}
    - Par: {course_info['par']}
    - Weekday Price: ${course_info['weekday_price']}
    - Weekend Price: ${course_info['weekend_price']}
    - Amenities: {course_info['amenities']}
    - Description: {course_info['description']}
    
    Provide helpful, concise responses about the course. If asked about something not in the data, 
    suggest contacting the course directly at {course_info['phone']}.
    """
    
    # Display chat history
    for message in st.session_state.chat_history:
        role = message["role"]
        content = message["content"]
        
        if role == "user":
            st.write(f"You: {content}")
        else:
            st.write(f"Assistant: {content}")
    
    # Chat input
    user_input = st.text_input("Type your question here:", key=f"chat_input_{course_name}")
    
    if user_input:
        # Add user message to history
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Prepare messages for API
        messages = [
            {"role": "system", "content": system_message},
        ]
        messages.extend(st.session_state.chat_history)
        
        # Get AI response
        ai_response = get_ai_response(messages)
        
        # Add AI response to history
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
        
        # Rerun to update chat display
        st.rerun()
    
    # Clear chat button
    if st.button("Clear Chat", key=f"clear_chat_{course_name}"):
        st.session_state.chat_history = []
        st.rerun()
