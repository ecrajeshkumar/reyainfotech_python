# planner.py

from config import client, model_1

def choose_best_tool(user_request):
    planner_prompt = f"""
        You are an AI planner. 
        Available tools: ['get_current_time', 'roll_dice', 'generate_password', 'read_text_file']
        if the user's request is related to time, use 'get_current_time'.
        if the user's request is related to rolling a dice, use 'roll_dice'.
        if the user's request is related to generating a password, use 'generate_password'.
        if the user's request is related to reading a text file, use 'read_text_file'.
        if the user's request does not match any of the available tools, respond with 'none.'
        User request: '{user_request}'
        """
    
    response = client.chat.completions.create(
        model=model_1,
        messages=[
            {"role": "system", "content": "You are an AI planner."},
            {"role": "user", "content": planner_prompt}
        ]
    )
    return response.choices[0].message.content.strip()
    