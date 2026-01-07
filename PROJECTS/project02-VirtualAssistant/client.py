# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv("../../env/.env")
# api = os.getenv("OPENAI_API_KEY")

# client = OpenAI(
#     api_key=api
# )

# completion = client.chat.completions.create(
#     model = "gpt-3.5-turbo",
#     messages=[
#         {"role": "system" , "content":"You are a poetic assitant, skilled in explaining complex programming concepts with cretaive flair. "},
#         {"role": "user", "content":"Compose a poem that explains the concept of recursion in programming"}
#     ]
# )

# print(completion.choices[0].message.content)