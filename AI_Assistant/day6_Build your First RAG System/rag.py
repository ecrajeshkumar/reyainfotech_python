# from openai import OpenAI
# from dotenv import load_dotenv
# import os

from similarity import cosine_similarity
from config import client, model_1, model_2

from retriever import load_documents
from embedding import create_embedding
from similarity import cosine_similarity

print("="*40)
print("============= My AI Assistant =============")
print("="*40)

documents = load_documents()
document_embeddings = {}
for filename, content in documents.items():
    embedding = create_embedding(content)
    document_embeddings[filename] = embedding

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("nAI  : Goodbye! Have a great day.")
        break

    user_embedding = create_embedding(user_input)

    # best_match = None
    # highest_similarity = -1
    best_score = -1
    best_document = None

    for filename, embedding in document_embeddings.items():
        score = cosine_similarity(user_embedding, embedding)
        if score > best_score:
            best_score = score
            best_document = filename
    
    print("="*40)
    if best_document:
        print(f"Best match found in file: {best_document}")
        print(f"Content: {documents[best_document]}")
    else:
        print("No relevant documents found.")
    print("="*40)

    context = documents[best_document]
    prompt = f"Context: {context}\n\nUser: {user_input}\nAI:"
    response = client.chat.completions.create(
        model = model_1,
        messages = [{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
    )
    print(f"AI  : {response.choices[0].message.content}")