from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import MistralAIEmbeddings

embeddings = MistralAIEmbeddings(
    model = 'mistral-embed'
)

text = [
    "Hello this is Rohan  Jangir",
    "Hello your name is YouTube",
    "And you all are very beautifull"
]
vector = embeddings.embed_documents(text)

print(len(vector))