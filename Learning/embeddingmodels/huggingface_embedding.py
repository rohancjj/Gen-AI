from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

embeddings = model.encode([
    "Machine learning is powerful",
    "Deep learning is a subset of ML"
])

print(len(embeddings[0]))  # vector size (384)
