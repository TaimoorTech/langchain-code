from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# dimensions means the size of the embedding vector. The larger the dimensions, the more information can be captured in the embedding, but it also requires more computational resources.

embedding = OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=32
)

#  single query embedding
# result = embedding.embed_query("What is the capital of Pakistan?")

# print(str(result))

# multiple queries embedding
documents = [
    "What is the capital of Pakistan?",
    "What is the capital of Sindh?",
    "What is the capital of Punjab?",
]
result = embedding.embed_documents(documents)
print(str(result))