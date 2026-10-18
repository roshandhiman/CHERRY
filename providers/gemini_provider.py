import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing from .env")
client=genai.Client(api_key=api_key)
def get_gemini_client():
    return client
def ask_gemini(message:str)->str:
    response=client.models.generate_content(
        model="gemini-2.5-flash",contents=message
    )
    return response.text