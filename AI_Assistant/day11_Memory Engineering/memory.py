import json
import sqlite3

import numpy as np
from config import *

DATABASE = "memory.db"


def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            assistant_message TEXT,
            embedding TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()

# Converting text into numerical vectors. If words in text are similar then it generate similar numerical value for that words.
# "Dog is playing. puppy is eating.". Here Dog and puppy is close so it generate two numerical value like ~0.85–0.89, 
# playing and eating these two words are different so it generate two different numerical value not similar ~0.3–0.8.
def create_embedding(text):
    response = client.embeddings.create(
        model = model_2,
        input = text
    )
    return response.data[0].embedding

# It measure how similar two vectors are in terms of their direction, regardless of their magnitude.
# It provide a numerical measure of similarity between two sets of values, focusing on their orientation rather than their size.
# print(cosine_similarity([1, 0], [0, 1]))   # 0.0 (orthogonal)
# print(cosine_similarity([1, 1], [2, 2]))   # 1.0 (same direction)
# print(cosine_similarity([1, 0], [-1, 0]))  # -1.0 (opposite)
def cosine_similarity(vector1, vector2):
    v1 = np.array(vector1)
    v2 = np.array(vector2)

    return np.dot(v1, v2) / (
        np.linalg.norm(v1) *
        np.linalg.norm(v2)
    )


def save_memory(user_message, assistant_message):
    text = user_message + "\n" + assistant_message

    embedding = create_embedding(text)
    
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO memories
        (
            user_message,
            assistant_message,
            embedding
        )
        VALUES (?, ?, ?)
        """,
        (
            user_message,
            assistant_message,
            json.dumps(embedding)
        )
    )

    connection.commit()
    connection.close()


def search_semantic_memories(
    query,
    top_k = 3,
    threshold = 0.20
):
    query_embedding = create_embedding(query)

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            user_message,
            assistant_message,
            embedding,
            created_at
        FROM memories
    """)

    rows = cursor.fetchall()

    connection.close()

    results = []

    for (
        user_message,
        assistant_message,
        embedding_json,
        created_at
    ) in rows:

        memory_embedding = json.loads(
            embedding_json
        )

        score = cosine_similarity(
            query_embedding,
            memory_embedding
        )
        
        if score >= threshold:
            results.append({
                "user_message": user_message,
                "assistant_message": assistant_message,
                "created_at": created_at,
                "score": score
            })

    results.sort(
        key = lambda item: item["score"],
        reverse=True
    )

    #print(results)

    return results[:top_k]

def save_semantic_memory(fact):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    embedding = create_embedding(fact)

    cursor.execute(
        """
        INSERT INTO memories
        (
            user_message,
            assistant_message,
            embedding
        )
        VALUES (?, ?, ?)
        """,
        (
            fact,
            "",
            json.dumps(embedding)
        )
    )

    connection.commit()
    connection.close()


