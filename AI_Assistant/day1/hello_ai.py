from openai import OpenAI
# This imports the library that allows python to interact with the OpenAI API (AI model). 
from dotenv import load_dotenv
# This imports the library that allows python to read environment variables from a .env file.
import os
# This imports the library that allows python to interact with the operating system, such as reading environment variables.
load_dotenv()
# Load configuration from .env file


# Read everything from environment variables
base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
model = os.getenv("MODEL")

client = OpenAI(
    base_url = base_url,
    api_key = api_key
)

print("="*40)
print("=== AI Assistant ===")
print("="*40)

# Send a question to the AI model and get a response
response = client.chat.completions.create(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the capital of Bihar?"
        }
    ]
)

# Print the AI's response
print(response.choices[0].message.content)
