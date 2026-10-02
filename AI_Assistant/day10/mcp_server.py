from fastmcp import FastMCP

mcp = FastMCP("AI MCP SErver")

from datetime import datetime
@mcp.tool()
def current_time():

    """Return the current date and time."""

    return datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )


import random
@mcp.tool()
def roll_dice():

    """Roll a six-sided dice."""

    return random.randint(1,6)

import secrets
import string
@mcp.tool()
def generate_password(length: int = 12):

    """
    Generate a secure password.
    """

    alphabet = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    return "".join(
        secrets.choice(alphabet)
        for _ in range(length)
    )


import requests
@mcp.tool()
def get_weather(city: str):
    """Get current weather for a city."""
    url = f"https://wttr.in/{city}?format=3"
    return requests.get(url).text

@mcp.tool()
def calculate(expression: str):
    """Evaluate a math expression safely."""
    return eval(expression, {"__builtins__": {}})


import random
@mcp.tool()
def random_quote():
    """Return a motivational quote."""
    quotes = [
        "Stay hungry, stay foolish.",
        "The best way to predict the future is to invent it.",
        "Success is not final, failure is not fatal."
    ]
    return random.choice(quotes)

import uuid
@mcp.tool()
def generate_uuid():
    """Generate a unique identifier."""
    return str(uuid.uuid4())

@mcp.tool()
def summarize(text: str):
    """Summarize given text."""
    sentences = text.split(".")
    return sentences[0] + "..." if len(sentences) > 1 else text


if __name__ == "__main__":
    print("Starting MCP server..")
    mcp.run()

