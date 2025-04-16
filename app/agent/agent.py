# app/agent/agent.py

import os
import openai
from app.agent import tools
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Tool mapping for dispatching
TOOL_FUNCTIONS = {
    "schedule_meeting": tools.schedule_meeting,
    "summarize_text": tools.summarize_text,
    "format_email_response": tools.format_email_response
}

def agent_respond(user_input: str) -> str:
    """
    Uses GPT to decide what to do, and either responds directly
    or calls one of the available tools.
    """
    system_prompt = """
You are BusinessBot, a helpful assistant that automates business tasks.
You can call the following tools using the format: 
TOOL: tool_name | PARAMS: param1=value1, param2=value2

Available tools:
- schedule_meeting(participant, date, time)
- summarize_text(text)
- format_email_response(name, topic)

Only respond with TOOL and PARAMS if a tool is needed.
Otherwise, answer normally.
"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.2
    )

    reply = response["choices"][0]["message"]["content"].strip()
    
    if reply.startswith("TOOL:"):
        tool_name, param_line = reply.split("|")
        tool_name = tool_name.replace("TOOL:", "").strip()
        param_line = param_line.replace("PARAMS:", "").strip()

        # Parse parameters into a dictionary
        params = {}
        for pair in param_line.split(","):
            key, value = pair.split("=")
            params[key.strip()] = value.strip()

        tool_fn = TOOL_FUNCTIONS.get(tool_name)
        if tool_fn:
            result = tool_fn(**params)
            return f"(Used tool `{tool_name}`)\n{result}"
        else:
            return "Sorry, I don’t recognize that tool."
    
    else:
        return reply
