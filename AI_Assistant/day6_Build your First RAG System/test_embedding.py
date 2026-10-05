from openai import OpenAI
# This imports the library that allows python to interact with the OpenAI API (AI model). 
from dotenv import load_dotenv
# This imports the library that allows python to read environment variables from a .env file.
import os
# This imports the library that allows python to interact with the operating system, such as reading environment variables.
from similarity import cosine_similarity


load_dotenv()
# Load configuration from .env file

# # Read everything from environment variables
base_url = os.getenv("BASE_URL")
api_key = os.getenv("API_KEY")
# for MODEL_1 is for chat and MODEL_2 is for embedding
model_1 = os.getenv("MODEL_1")
model_2 = os.getenv("MODEL_2")

client = OpenAI(
    base_url = base_url,
    api_key = api_key
)

text1 = "Python is a programming language."
text2 = "Python is used for software development."

embedding1 = client.embeddings.create(
    model = model_2,
    input = text1,
).data[0].embedding

embedding2 = client.embeddings.create(
    model = model_2,
    input = text2,
).data[0].embedding

print(len(embedding1))
print(len(embedding2))
# print("Embedding for text1:", embedding1)
# print("Embedding for text2:", embedding2)

score = sum(a * b for a, b in zip(embedding1, embedding2))
print("Similarity score:", score)

score = cosine_similarity(embedding1, embedding2)
print("Cosine similarity score:", score)
