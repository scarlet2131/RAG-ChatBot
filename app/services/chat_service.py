from app.crud.embedding import search_relevant_documents
from app.services.chunking_service import spacy_chunking
import sentence_transformers

from app.services.gpt_integration_service import get_response_with_chatgpt

model = sentence_transformers.SentenceTransformer('all-MiniLM-L6-v2')

def process_input(user_input):
    chunks = spacy_chunking(user_input)
    embeddings = model.encode(chunks)
    print("error here? 3 ")

    relevant_doc = search_relevant_documents(embeddings)
    print("error here? 4 ")

    return relevant_doc

def chat_response(user_input):
    rag_response = process_input(user_input)
    print("error here? 1 ")
    gpt_response = get_response_with_chatgpt(user_input, rag_response)
    print("error here? 2 ")

    return gpt_response



