import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json
from pydantic import BaseModel, Field
from typing import Optional


load_dotenv()

api_key = os.getenv("api_key")

client = OpenAI(
    api_key=api_key, 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

def run_command(cmd:str):
    # result = os.system(cmd)
    result = os.system(cmd)
    return result

def get_weather(city:str):
    url = f"https://wttr.in/{city.lower()}?format=%C=%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "somthing went wrong"



available_tools = {
    "get_weather" : get_weather,
    "run_command" : run_command,
}

SYSTEM_PROMPT = """
    You are an expert AI Assistant in resolving user queries using chain of thought.
    You work on START. PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also call a tool if required from the list of available tools.
    For every tool call wait for the observe step which is the output from the called tool.

    Rules:
    - Strictly follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (Which is going to the displayed to the user).
    - Do not output markdown code blocks or plain text, only output raw JSON.

    Output JSON Format:
    {"step": "START" | "PLAN" | "OUTPUT" | "TOOL , "content": "string", "tool": "string", "input": "string"}

    Available Tools:
    - get_weather(city: str): Takes city name as an input string and returns the weather info about city
    -run_command(cmd: str): takes a system linux command as string and executes the command on user's system and returns the output from the command

    Example 1:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: {"step":"PLAN", "content": "Seems like user is interested in meth problem"}
    PLAN: {"step":"PLAN", "content": "looking at the problem, we should solve this using BODMAS method"}
    PLAN: {"step":"PLAN", "content": "Yes, The BODMAS is correct thing to be done here"}
    PLAN: {"step":"PLAN", "content": "first we must multiply 3 * 5 which is 15"}
    PLAN: {"step":"PLAN", "content": "Now the new equation is 2 + 15 / 10"}
    PLAN: {"step":"PLAN", "content": "We must perform divide that is 15/10 = 1.5"}
    PLAN: {"step":"PLAN", "content": "Now the new equation is 2 + 1.5"}
    PLAN: {"step":"PLAN", "content": "Now finally lets perform the add 3.5"}
    PLAN: {"step":"PLAN", "content": "Great, we have solved and finally left with 3.5 as ans"}
    OUTPUT: {""step":"OUTPUT": "content": "3.5"}


    Example 2:
    START: What is the weather of Delhi?
    PLAN: {"step":"PLAN", "content": "Seems like user is interested in getting weather of Delhi in India"}
    PLAN: {"step":"PLAN", "content": "Lets see if we have any available tool from the list of available tools"}
    PLAN: {"step":"PLAN", "content": "Great, we have get_weather tool available for the query."}
    PLAN: {"step":"PLAN", "content": "I need to call get_weather tool for delhi as input for city"}
    PLAN: {"step":"TOOL", "tool":'get_weather', "input": "Delhi"}
    PLAN: {"step":"OBSERVE", "tool":'get_weather', "output": "The temp of Delhi is cloudybwith 20C"}
    PLAN: {"step":"PLAN", "content": "Great. I got the weather info about Delhi"}
    OUTPUT: {""step":"OUTPUT": "content": "The current weather in Delhi is 20C with some cloudy sky"}

"""

print("\n\n\n")

class LLMOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL, etc")
    content: Optional[str] = Field(None, description='The optional string contentfor the step')
    tool: Optional[str] = Field(None, description="The ID of the tool to call")
    input:Optional[str] = Field(None, description="The input params for the tool")

message_history = [{'role': 'system', 'content': SYSTEM_PROMPT}]

while True:
    user_query = input("> ")
    message_history.append({"role": "user", "content": user_query})


    while True:
        response = client.chat.completions.parse(
            model='gemini-3.5-flash-lite',
            # model='gemini-3.8-flash',
            response_format=LLMOutputFormat,
            messages=message_history
        )

        raw_result = response.choices[0].message.content
        message_history.append({'role': 'assistant', 'content': raw_result})
        
        try:
            # parsed_result = json.loads(raw_result)
            parsed_result = response.choices[0].message.parsed
        except json.JSONDecodeError:
            print("Invalid JSON received:", raw_result)
            break

        if parsed_result is None:
            print("Model did not return valid JSON. Raw output was:", raw_result)
            # Aap chahein toh yahan user message bhej kar dobara try karwa sakte hain
            message_history.append({'role': 'user', 'content': 'Please respond strictly in the required JSON format.'})
            continue

        step = parsed_result.step
        content = parsed_result.content

        if step == "START":
            print('Starting:', content)
        if step == "TOOL":
            tool_name = parsed_result.tool
            tool_input = parsed_result.input
            print(f'Tool: {tool_name} {tool_input}' )

            tool_response = available_tools[tool_name](tool_input)
            # message_history.append({"role":"developer", "content": json.dumps({"step":"OBSERVE","tool": "tool_to_call", "input": tool_input, "output": tool_response})})
            message_history.append({
                "role": "developer", 
                "content": json.dumps({
                    "step": "OBSERVE",
                    "tool": tool_name, 
                    "input": tool_input, 
                    "output": tool_response
                })
            })
            
            message_history.append({'role': 'user', 'content': 'Continue with the next step based on the tool output.'})
            continue
        
        elif step == "PLAN":
            print('Thinking:', content)
        elif step == "OUTPUT":
            print('Result:', content)
            break

        # Gemini ko next turn trigger karne ke liye user message zaroori hai:
        message_history.append({'role': 'user', 'content': 'Continue with the next step.'})

print("\n\n\n")