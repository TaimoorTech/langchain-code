from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=300,
)

documents = [
    "Babar azam is a Pakistani cricketer who is known for his exceptional batting skills and consistency in international cricket.",
    "Shahid Afridi is a former Pakistani cricketer and captain of the national team, famous for his aggressive batting style and record-breaking performances in limited-overs cricket.",
    "Shoaib Akhtar is a retired Pakistani fast bowler, renowned for his incredible pace and ability to bowl consistently at speeds exceeding 150 km/h.",
    "Shaheen Shah Afridi is a young Pakistani cricketer who has made a name for himself as a talented fast bowler and has represented the national team in various formats of the game.",
    "Misbah-ul-Haq is a former Pakistani cricketer and captain, known for his calm demeanor, strategic approach to the game, and ability to anchor the innings in Test cricket.",
]

query = "Tell me about BABAR AZAM"

# Generate embeddings for the documents and the query
document_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# Calculate cosine similarity between the query embedding and each document embedding
# [0] is used to get the first (and only) row of the resulting similarity matrix
scores = cosine_similarity([query_embedding], document_embeddings)[0]

# Print the similarity scores along with their corresponding document indices
# print(list(enumerate(scores)))

# Find the index of the document with the highest similarity score
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1], reverse=True)[0]

print(query)
print(documents[index])
print(f"Similarity Score: {score:.4f}")