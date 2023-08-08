import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])

generated_message = chat_completion.choices[0].message['content']

print("Assistant message: ", generated_message)