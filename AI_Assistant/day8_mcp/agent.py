import asyncio
from config import *
from client import *


# Build Tool Descriptions
def build_tool_descriptions(tools):
    """
    Build a dictionary of tool descriptions from the list of tools.
    """
    tool_descriptions = ""
    for tool in tools:
        #tool_descriptions[tool.name] = tool.description
        tool_descriptions += f"""
                Tool Name: {tool.name}
                Description: {tool.description}
            """
    return tool_descriptions

def planner(user_request, tools):
    tool_descriptions = build_tool_descriptions(tools)

    ###Then create a prompt by combining user input and Tool Description.  
    # and Give this prompt to Ollama. ###

    prompt = f"""
        you are an AI assistant. You have access to the following tools:
        {tool_descriptions}
        Instructions
        1. Select the best tool.
        2. Reply ONLY with the tool name.
        3. Do not explain.

        User Request: {user_request}
    """
    # Give this prompt to Ollama and get the tool name.
    response = client.chat.completions.create(
        model = model_1,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
    )
    #Ollama returns the tool name
    tool_name = response.choices[0].message.content
    return tool_name.strip()  # Return the tool name without any leading/trailing whitespace

def generate_response(user_request, tool_result):
    """
    Generate a natural language response based on the user request and tool result.
    """
    prompt = f"""
        You are an AI assistant. 
        User Request: {user_request}
        Tool Result: {tool_result}
        Instructions:
        1. Generate a natural language response to the user request based on the tool result.
        2. Do not include any tool names or technical details in the response.
        Respond directly to the user in a natural, conversational way.
        Use the tool result as the factual source.
        Transform raw tool output into a human-friendly answer.
        Do not simply copy raw values when a natural sentence would be better.
        Do not add information that is not needed to answer the request.
        Do not mention tools, internal processing, planning, or reasoning.
        Keep the response concise.
    """
    # Give this prompt to Ollama and get the final answer.
    response = client.chat.completions.create(
        model = model_1,
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
    )
    final_answer = response.choices[0].message.content
    return final_answer.strip()  # Return the final answer without any leading/trailing whitespace

async def main():
    # Step 1: Connect to the MCP Server.
    client = await connect_to_server()

    # Step 2: Discover available tools on the server.
    tools = await discover_tools(client)
    # print("Available Tools")
    # print("----------------")
    # for tool in tools:
    #     print(tool.name)
    # print("----------------")

    ### Step 3: Planner: Take the User Input (Question). Create Tool Descriptions for each tool. 
    # Then create a prompt by combining user input and Tool Description.  and Give this prompt 
    # to Ollama. ###
    user_request = input("User : ")
    tool_name = planner(user_request, tools)

    ### Step 4: Execute the selected tool on the server. ###
    tool_result = await execute_tools(client, tool_name)

    # Step 5: Generate a natural language response.
    final_answer = generate_response(user_request, tool_result)
    print(final_answer)

    await disconnect(client)

if __name__ == "__main__":
    asyncio.run(main())