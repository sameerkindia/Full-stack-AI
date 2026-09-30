# from openai import OpenAI
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('api_key')

client = genai.Client(api_key=api_key)

response = client.interactions.create(
    model="gemini-3.6-flash",
    input="Explain how AI works in a few words"
)

print(response.output_text)