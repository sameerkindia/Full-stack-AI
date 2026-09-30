import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key= os.getenv("api_key")

client = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[
        {"role": 'user', "content": 'Tell me a joke in Hinglish'}
        ]
)

print(response.choices[0].message.content)