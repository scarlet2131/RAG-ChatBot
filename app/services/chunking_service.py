# doing contextual chunking
import spacy
import fitz
import sentence_transformers

from app.crud.embedding import store_chunks_in_db

# Load the pre-trained model
model = sentence_transformers.SentenceTransformer('all-MiniLM-L6-v2')

# contextual chunking
# Load spaCy's small English model
nlp = spacy.load("en_core_web_sm")

def spacy_chunking(text, max_chunk_size=512):
    doc = nlp(text)
    # print(doc)
    chunks = []
    chunk = ""
    count = 0
    for sentence in doc.sents:
        # if count<4:
        #     print('is sents',sentence.text)
        # count +=1
        if len(chunk) + len(sentence.text)+1<= max_chunk_size:
            chunk += " "+ sentence.text
        else:
            chunks.append(chunk.strip())
            chunk = sentence.text
    if chunk:
        chunks.append(chunk)

    return chunks


# text extraction from pdf
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# pdf_path = "/Users/monisharanjan/PycharmProjects/Chatbot-RAG/budget-2024.pdf"
# pdf_text = extract_text_from_pdf(pdf_path)
# # print(pdf_text)
# chunks = spacy_chunking(pdf_text)
# print(len(chunks))
#
# # Generate embeddings
# embeddings = model.encode(chunks)
# print(type(embeddings))
# store_chunks_in_db(chunks, embeddings)

