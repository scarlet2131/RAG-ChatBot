import numpy as np
import torch
from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine_similarity

from app.db.base import get_database

def store_chunks_in_db(chunks, embeddings):
    db = get_database()
    collection = db['documents']
    data = [{"text" : chunk , "embedding" : embedding.tolist()} for chunk, embedding in zip(chunks, embeddings)]
    collection.insert_many(data)
    print(f"Inserted {len(data)} documents into MongoDB.")


def cosine_similarity(user_embedding, embeddings):
    # Ensure inputs are tensors
    if not isinstance(user_embedding, torch.Tensor):
        user_embedding = torch.tensor(user_embedding)
    if not isinstance(embeddings, torch.Tensor):
        embeddings = torch.tensor(embeddings)

    # Normalize embeddings to have unit norm
    user_embedding = user_embedding / user_embedding.norm(dim=1, keepdim=True)
    embeddings = embeddings / embeddings.norm(dim=1, keepdim=True)

    # Compute cosine similarity
    return torch.mm(user_embedding, embeddings.t())


def search_relevant_documents(user_embedding):
    db = get_database()
    collection = db['documents']
    documents = list(collection.find())
    embeddings = np.array([doc['embedding'] for doc in documents])

    # Convert numpy arrays to PyTorch tensors
    user_embedding_tensor = torch.tensor(user_embedding)
    embeddings_tensor = torch.tensor(embeddings)


    similarities = sklearn_cosine_similarity(user_embedding_tensor.numpy().reshape(1, -1), embeddings_tensor.numpy())
    return similarities


