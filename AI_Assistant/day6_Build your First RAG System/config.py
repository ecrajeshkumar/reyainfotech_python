# config.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Read values from environment variables
base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
model_1 = os.getenv("MODEL_1")  # chat model
model_2 = os.getenv("MODEL_2")  # embedding model

# Initialize client once
client = OpenAI(base_url = base_url, api_key = api_key)
