from config import *


def extract_memory(
    user_message,
    assistant_message
):
    prompt = f"""
You are a memory extraction system.

Read the conversation below and determine whether
it contains useful long-term information about the user.

User:
{user_message}

Assistant:
{assistant_message}

Store information only if it will be useful
in future conversations.

Useful information includes:
- preferences
- interests
- goals
- skills
- projects
- important user facts

Do NOT store:
- temporary questions
- current time
- random calculations
- one-time requests
- tool results
- casual conversation

If useful information exists,
return ONLY the fact that should be remembered.

If there is nothing useful to remember,
return:

NONE
"""

    response = client.chat.completions.create(
        model = model_1,
        messages = [
            {
                "role": "system",
                "content": (
                    "You extract useful long-term memories."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()