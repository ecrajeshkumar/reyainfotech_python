from openai import OpenAI
# This imports the library that allows python to interact with the OpenAI API (AI model). 
from dotenv import load_dotenv
# This imports the library that allows python to read environment variables from a .env file.
import os
# This imports the library that allows python to interact with the operating system, such as reading environment variables.

load_dotenv()
# Load configuration from .env file

from tools import (
    get_current_time,
    roll_dice,
    generate_password,read_text_file)

from tool_manager import execute_tool

# Read everything from environment variables
base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
model = os.getenv("MODEL_1")

client = OpenAI(
    base_url = base_url,
    api_key = api_key
)

print("="*40)
print("============= AI Assistant =============")
print("="*40)


roles = {
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",

    "2": "You are a senior Python developer. Explain programming concepts clearly and always include Python examples.",

    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",

    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",

    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}

print("\nChoose Your Assistant")
print("1. Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")
choice = input("\nEnter your choice : ")

conversation_history = [
    {
        "role": "system",
        "content": roles.get(
            choice,
            "You are a helpful AI assistant."
        )
    }
]

while True:
    user_input = input("You: ")
    # Save the user's message
    
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the AI Assistant. Goodbye!")
        break
    
    # Check if the user input matches any tool commands
    tool_result = execute_tool(user_input)
    if tool_result:
        print("\nAI :", tool_result)
        continue
    
    # Direct handle with tools.py functions for specific file related commands
    text = user_input.lower()
    if text.startswith("summarize "):
        filename = user_input[10:].strip()
        file_content = read_text_file("data/" + filename)

        prompt = f"""
        Summarize the following document.

        Document:

        {file_content}
        """

        response = client.chat.completions.create(
            model = model,
            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        print(response.choices[0].message.content)
        continue

    if text.startswith("explain"):
        filename = user_input[8:].strip()
        file_content = read_text_file("data/" + filename)

        prompt = f"""
        Explain the following document.

        Document:

        {file_content}
        """

        response = client.chat.completions.create(
            model = model,
            messages = [
                {
                    "role":"system",
                    "content":"You are a helpful assistant."
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )
        print(response.choices[0].message.content)
        continue
    # type on terminal in this formate
    # You: ask project.txt Who worked on the project?
    if text.startswith("ask"):
        parts = user_input.split(maxsplit=2)
        #print(parts)
        filename = parts[1]
        question = parts[2]

        file_content = read_text_file("data/" + filename)

        prompt = f"""
            You are given a document.
            Answer the user's question using
            only the information present
            in the document.
            If the answer is not available,
            say:
            'I couldn't find that information
            in the document.'
            Document:
            {file_content}
            Question:
            {question}
        """

        response = client.chat.completions.create(
            model = model,
            messages = [
                {
                    "role":"system",
                    "content":"You are a helpful assistant."
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )
        print(response.choices[0].message.content)
        continue

    # Add/Save the user's message to the conversation history
    conversation_history.append(
        {"role": "user", 
        "content": user_input
        }
    )

    # Send a question to the AI model and get a response
    response = client.chat.completions.create(
        model = model,
        messages = conversation_history
    )
    
    ai_reply = response.choices[0].message.content

    # Print the AI's response
    print("\nAI:", ai_reply)

    # Add/Save the AI's response to the conversation history
    conversation_history.append(
        {"role": "assistant", 
        "content": ai_reply
        }
    )

