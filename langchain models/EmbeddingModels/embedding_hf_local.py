from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# text = "Islamabad is the capital of Pakistan."

# vector = embedding.embed_query(text)

documents = [
    "What is the capital of Pakistan?", 
    "What is the capital of Sindh?",
    "What is the capital of Punjab?",
    ]

vector = embedding.embed_documents(documents)
print(f"Embedding vector for the text: {vector}")