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
print("============= AI Assistant =============")
print("="*40)

# # Store the conversation history
# conversation_history = [
#     {
#         "role": "system",
#         "content": "You are a friendly AI teacher. Explain every concept in simple language with real-life examples."
#     }
# ]

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
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the AI Assistant. Goodbye!")
        break

    # Add/Save the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Send a question to the AI model and get a response
    response = client.chat.completions.create(
        model = model,
        messages = conversation_history
    )

    
    ai_reply = response.choices[0].message.content
    # Print the AI's response
    print("\nAI:", ai_reply)

    # Add/Save the AI's response to the conversation history
    conversation_history.append({"role": "assistant", "content": ai_reply})


# print("\n========== Conversation History ==========")
# for conversation in conversation_history:
#     print(f"{conversation['role'].title()} : {conversation['content']}")
# print("==========================================")




