import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv  

load_dotenv()  

st.title("Chatbot AI")

prompt = st.text_input("Enter your prompt:")


if st.button("Submit"):
    my_api_key = os.getenv("GOOGLE_API_KEY")  
    
    if not my_api_key:
        st.write("Error: API key not found. Please ensure it is set in the .env file.")
    else:
        try:
            genai.configure(api_key=my_api_key)

            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(prompt)
            st.write(response.text)

        except Exception as e:
            st.write(f"An error occurred: {e}")
