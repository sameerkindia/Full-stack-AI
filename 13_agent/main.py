import os
from dotenv import load_dotenv
from openai import OpenAI
import requests

load_dotenv()

api_key = os.getenv('api_key')

def getWeather(city:str):
    url = f"https://wttr.in/{city.lower()}?format=%C=%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "somthing went wrong"

print(getWeather("Pali"))

def main():
    userQuery = input("> ")

    client = OpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    response = client.chat.completions.create(
        model='gemini-3.6-flash',
        messages=[
            {'role': 'user', 'content': userQuery},
        ]
    )

    print(response.choices[0].message.content)


main()