from config import *

def research(task):
    prompt = f"""
You are a research agent. Your task is to gather information and insights related to the following task: {task}
Please provide a detailed summary of your research findings, including relevant information, references, 
and any insights that may help in the development of a solution for the task. Your response should be clear, concise, 
and well-structured.
Task: {task}
provide:
1. Important concepts
2. Key facts
3. Relevant examples

Keep the response concise and useful
for another AI agent.
"""
    response = client.chat.completions.create(
        model = model_1,
        messages = [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content