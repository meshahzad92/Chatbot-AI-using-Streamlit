import google.generativeai as genai
import os
from dotenv import load_dotenv  

# Load environment variables from the .env file
load_dotenv()  

my_api_key = os.getenv("GOOGLE_API_KEY")  
try:
    genai.configure(api_key=my_api_key)

    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt=input("Enter the prompt: ")
    response = model.generate_content(prompt)
    print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")

