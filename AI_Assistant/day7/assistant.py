# assistant.py

from config import client, model_1
from planner import choose_best_tool
from tools import get_current_time, roll_dice, generate_password, read_text_file

print("="*40)
print("============= My AI Assistant =============")
print("="*40)

while True:
    user_request = input("\nEnter your request (or type 'exit' to quit): ")

    if user_request.lower() == "exit":
        print("Exiting the assistant. Goodbye!")
        break

    # Use the planner to choose the best tool
    chosen_tool = choose_best_tool(user_request)

    if chosen_tool == "get_current_time":
        result = get_current_time()
    elif chosen_tool == "roll_dice":
        result = roll_dice()
    elif chosen_tool == "generate_password":
        result = generate_password()
    elif chosen_tool == "read_text_file":
        filename = input("Enter the filename to read: ")
        result = read_text_file(filename)
    else:
        result = "No suitable tool found for your request."

    prompt = f"""User request: '{user_request}'\nChosen tool: '{chosen_tool}'\nResult: '{result}'
            Answer the user naturally. don't add anything from your side in the answer. if tool is none, 
            then answer it from llm model.
         """

    response = client.chat.completions.create(
        model = model_1,
        messages = [
            {"role": "user", "content": prompt}
        ]
    )
    print("\nAI :", response.choices[0].message.content)