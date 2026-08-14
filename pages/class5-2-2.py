import openai    # pip install openai
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 初始化對話歷史
messages = [
    {"role": "system", "content": "Please use English to have the conversation"},
]

while True:
    user_inputs = input("You: ")  # Get user input
    if user_inputs.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_inputs})

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
    )
    assistant_message = response.choices[0].message.content
    print(f"AI: {assistant_message}")

    messages.append({"role": "assistant", "content": assistant_message})