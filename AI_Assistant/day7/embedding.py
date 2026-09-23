
from similarity import cosine_similarity
from config import client, model_2


def create_embedding(content):
    embedding1 = client.embeddings.create(
    model = model_2,
    input = content
    ).data[0].embedding
    return embedding1
