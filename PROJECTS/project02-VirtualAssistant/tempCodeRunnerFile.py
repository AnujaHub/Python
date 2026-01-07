from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv("../../env/.env")
api = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key = api,
    base_url="https://openrouter.ai/api/v1"
)

completion = client.chat.completions.create(
    model = "mistralai/mistral-7b-instruct",
    messages=[
        {"role": "system" , "content":"You are a poetic assitant, skilled in explaining complex programming concepts with cretaive flair. "},
        {"role": "user", "content":"Compose a poem that explains the concept of recursion in programming"}
    ]
)

print(completion.choices[0].message.content)