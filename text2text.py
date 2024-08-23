import google.generativeai as genai
import os


try:
    
    genai.configure(api_key="AIzaSyBtkylRxKdz_LpNX-Y1KSnrsqF0kphu53M")

    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt=input("Enter the prompt: ")
    response = model.generate_content(prompt)
    print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")
