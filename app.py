import os
import openai
from dotenv import load_dotenv
import sys

# Load environment variables from .env file
load_dotenv()
# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chat_response(input_message):
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input_message}])

    #Access the generated response
    generated_response = chat_completion.choices[0].message['content']

    return generated_response

#Get user input from stdin (console)
for line in sys.stdin:
    user_input = line.strip()
    if user_input.lower() == "exit":
        break

    assistant_answer = get_chat_response(user_input)

    print("Assistant message: ", assistant_answer)

