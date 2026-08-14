import openai    # pip install openai
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
while True:
    user_inputs = input("You: ")  # Get user input
    if user_inputs.lower() in ["exit", "quit"]:
        break

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_inputs},
        ],
    )
    assistant_message = response.choices[0].message.content
    print(f"AI: {assistant_message}")