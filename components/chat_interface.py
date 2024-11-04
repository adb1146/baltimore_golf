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

def clear_chat():
    st.session_state.chat_history = []
    st.rerun()

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
    system_message = f'''You are a helpful golf course assistant for Baltimore area golf courses.
You have access to information about all courses and can help users find the right course for their needs.
Here are all the available courses and their details:

{courses_data}

Help users find suitable courses based on their preferences such as:
- Location/area
- Price range
- Amenities
- Difficulty level
- Special features

For each recommendation:
1. Suggest specific courses that match the user's criteria
2. Always ask if they would like to add the recommended courses to their selection
3. End your response with: "Would you like me to add [course name(s)] to your selection? (Yes/No)"'''

    # Chat input form
    with st.form(key='chat_form', clear_on_submit=True):
        cols = st.columns([5, 1])
        with cols[0]:
            user_input = st.text_input(
                "Type your question here:",
                placeholder="e.g., What courses have driving ranges?",
                key="chat_input",
                label_visibility="collapsed"
            )
        with cols[1]:
            submit_button = st.form_submit_button(
                "Send",
                use_container_width=True,
                type="primary"
            )

        if submit_button and user_input:
            # Add user message to history
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            
            # After getting AI response, check if user wants to add courses
            if user_input.lower() in ['yes', 'y']:
                # Get the last AI message
                last_ai_message = next((msg for msg in reversed(st.session_state.chat_history) 
                                    if msg['role'] == 'assistant'), None)
                if last_ai_message:
                    # Extract course names from the last recommendation
                    recommended_courses = [course['name'] for course in courses_info 
                                        if course['name'] in last_ai_message['content']]
                    if recommended_courses:
                        # Add courses to selection
                        current_selection = st.session_state.get('selected_courses', [])
                        new_courses = [c for c in recommended_courses if c not in current_selection]
                        if new_courses:
                            st.session_state['selected_courses'] = current_selection + new_courses
                            response = f"I've added {', '.join(new_courses)} to your selection."
                        else:
                            response = "These courses are already in your selection."
                    else:
                        response = "I couldn't find any courses to add from the last recommendation."
                    
                    # Add system message about course selection
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": response
                    })
                    st.rerun()
            else:
                # Prepare messages for API
                messages = [
                    {"role": "system", "content": system_message}
                ]
                messages.extend(st.session_state.chat_history[-5:])
                
                # Get AI response
                ai_response = get_ai_response(messages)
                
                # Add AI response to history
                st.session_state.chat_history.append({"role": "assistant", "content": ai_response})
                st.rerun()

    # Clear chat button
    st.button("Clear Chat", key="clear_chat", on_click=clear_chat)

    # Display chat history below the form
    if st.session_state.chat_history:
        for message in reversed(st.session_state.chat_history):  # Use reversed() to show newest first
            role = message["role"]
            content = message["content"]
            
            if role == "user":
                st.markdown(
                    "<div style='background-color: #e9ecef; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;'>"
                    f"<strong style='color: #1a1a1a;'>You:</strong><br>"
                    f"<span style='color: #1a1a1a;'>{content}</span>"
                    "</div>",
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    "<div style='background-color: #ffffff; padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border: 1px solid #dee2e6;'>"
                    f"<strong style='color: #1a1a1a;'>Assistant:</strong><br>"
                    f"<span style='color: #1a1a1a;'>{content}</span>"
                    "</div>",
                    unsafe_allow_html=True
                )
