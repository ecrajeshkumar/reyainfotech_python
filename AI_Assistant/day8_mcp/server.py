# server.py

from datetime import datetime
from fastmcp import FastMCP

mcp = FastMCP("Chat Agent Server")

@mcp.tool
def get_current_time():
    """Get the current time in ISO format."""
    return datetime.now().strftime("%d-%m-%y %H:%M:%S")

import random
@mcp.tool
def roll_dice():
    """Roll a six-sided dice and return the result."""
    return random.randint(1, 6)

import secrets
import string
@mcp.tool
def generate_password(length: int = 12):
    """Generate a secure random password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    print("Starting the FastMCP server...")
    mcp.run()
