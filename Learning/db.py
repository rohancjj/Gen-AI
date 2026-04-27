from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import chroma
from langchain_core.documents import Document

docs = [
    Document(page_content="Python is a versatile programming language used in data science, AI, and web development.", metadata={"topic": "python"}),
    Document(page_content="Pandas is a Python library for data manipulation using DataFrames and Series.", metadata={"topic": "pandas"}),
    Document(page_content="Neural networks are machine learning models inspired by the brain, used for deep learning tasks.", metadata={"topic": "neural_network"})
]

embeddings = MistralAIEmbeddings(
    model = 'mistral-embed'
)

vectorstore = chroma.from_documents(
    documents = docs,
    embedding = embeddings,
    persist_directory = "chroma-db"
)

text = [
    "Hello this is Rohan  Jangir",
    "Hello your name is YouTube",
    "And you all are very beautifull"
]
vector = embeddings.embed_documents(text)

print(len(vector))
