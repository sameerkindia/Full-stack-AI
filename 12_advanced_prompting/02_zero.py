import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("api_key")

client = OpenAI(
    api_key=api_key, 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )


# Zero shot prompting: Directly giving the inst to the model
SYSTEM_PROMPT = 'you are a standup comedian like Abhisek Upamanyu, and only tell jokes in Hinglish language. if the qurey is not about joke. then just say sorry main sirf joke suna sakta hoon'

response = client.chat.completions.create(
    model='gemini-3.6-flash',
    messages=[
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': 'tell a joke'},
    ]
)

print(response.choices[0].message.content)