import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello"}],
        temperature=0
    )
    print("GPT-4 access confirmed!")
except openai.error.InvalidRequestError as e:
    print("GPT-4 access not available.")
    print("Reason:", e)