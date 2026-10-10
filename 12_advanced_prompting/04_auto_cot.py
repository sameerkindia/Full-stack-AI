import os
from dotenv import load_dotenv
from openai import OpenAI
import json


load_dotenv()

api_key = os.getenv("api_key")

client = OpenAI(
    api_key=api_key, 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

SYSTEM_PROMPT = """
    You are an expert AI Assistant in resolving user queries using chain of thought.
    You work on START. PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    Rules:
    - Strictly follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (Which is going to the displayed to the user).

    Output JSON Format:
    {"step": "START" | "PLAN" | "OUTPUT" , "content": "string"}

    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: {"step":"PLAN", "content": "Seems like user is interested in meth problem"}
    PLAN: {"step":"PLAN", "content": "looking at the problem, we should solve this using BODMAS method"}
    PLAN: {"step":"PLAN", "content": "Yes, The BODMAS is correct thing to be done here"}
    PLAN: {"step":"PLAN", "content": "Yes, The BODMAS is correct thing to be done here"}
    PLAN: {"step":"PLAN", "content": "first we must multiply 3 * 5 which is 15"}
    PLAN: {"step":"PLAN", "content": "Now the new equation is 2 + 15 / 10"}
    PLAN: {"step":"PLAN", "content": "We must perform divide that is 15/10 = 1.5"}
    PLAN: {"step":"PLAN", "content": "Now the new equation is 2 + 1.5"}
    PLAN: {"step":"PLAN", "content": "Now finally lets perform the add 3.5"}
    PLAN: {"step":"PLAN", "content": "Great, we have solved and finally left with 3.5 as ans"}
    OUTPUT: {""step":"OUTPUT": "content": "3.5"}

"""

print("\n\n\n")

message_history = [{'role': 'system', 'content': SYSTEM_PROMPT}]

user_query = input("> ")
message_history.append({"role": "user", "content": user_query})

# while True:
#     response = client.chat.completions.create(
#         model='gemini-3.6-flash',
#         response_format={"type": "json_object"},
#         messages=message_history
#     )

#     raw_result = response.choices[0].message.content
#     message_history.append({'role': 'assistant', 'content': raw_result})
#     parsed_result = json.loads(raw_result)

#     if parsed_result.get('step') == "START":
#         print('Starting ', parsed_result.get('content'))
#         continue

#     if parsed_result.get('step') == "PLAN":
#         print('Thinking ', parsed_result.get('content'))
#         continue

#     if parsed_result.get('step') == "OUTPUT":
#         print('Result ', parsed_result.get('content'))
#         break

while True:
    response = client.chat.completions.create(
        model='gemini-3.8-flash',
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({'role': 'assistant', 'content': raw_result})
    
    try:
        parsed_result = json.loads(raw_result)
    except json.JSONDecodeError:
        print("Invalid JSON received:", raw_result)
        break

    step = parsed_result.get('step')
    content = parsed_result.get('content')

    if step == "START":
        print('Starting:', content)
    elif step == "PLAN":
        print('Thinking:', content)
    elif step == "OUTPUT":
        print('Result:', content)
        break

    # Gemini ko next turn trigger karne ke liye user message zaroori hai:
    message_history.append({'role': 'user', 'content': 'Continue with the next step.'})

print("\n\n\n")