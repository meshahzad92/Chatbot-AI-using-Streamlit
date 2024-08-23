import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv  

def load_api_key():
    load_dotenv()
    return os.getenv("GOOGLE_API_KEY")

def initialize_history():
    if "history" not in st.session_state:
        st.session_state.history = []

def handle_submission(prompt, model):
    try:
        response = model.generate_content(prompt)
        st.session_state.history.append({"prompt": prompt, "response": response.text})
        st.write(response.text)
    except Exception as e:
        st.write(f"An error occurred: {e}")

def display_buttons():
    col1, col2 = st.columns([3, 1])  

    with col1:
        submit_button = st.button("Submit")
    
    with col2:
        history_button = st.button("History")
            
    return submit_button, history_button

def display_chat_history():
    if st.session_state.history:
        st.write("### Chat History")
        for chat in st.session_state.history:
            st.write(f"**You:** {chat['prompt']}")
            st.write(f"**AI:** {chat['response']}")

def main():
    st.title("Chatbot AI")
    
    my_api_key = load_api_key()

    initialize_history()

    prompt = st.text_input("Enter your prompt:")

    submit_button, history_button = display_buttons()

    if submit_button:
        if not my_api_key:
            st.write("Error: API key not found. Please ensure it is set in the .env file.")
        else:
            try:
                genai.configure(api_key=my_api_key)
                model = genai.GenerativeModel('gemini-1.5-flash')
                handle_submission(prompt, model)
            except Exception as e:
                st.write(f"An error occurred: {e}")

    if history_button:
        display_chat_history()

if __name__ == "__main__":
    main()
