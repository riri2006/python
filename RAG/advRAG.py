from langchain_groq import ChatGroq
from llama_parse import LlamaParse
from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")
memory = MemorySaver()
agent = create_agent(
    model=llm,
    checkpointer=memory
)

path = input("Enter the path of file: ")

parser = LlamaParse(
    api_key=os.getenv("LLAMA_API_KEY"),
    result_type="markdown"
)
pdoc = parser.load_data(path)
for doc in pdoc:
    documents =[
        Document(
            page_content= doc.text
            # metadata={"source":"abc"}
        )
    ]

embedding = OllamaEmbeddings(model="nomic-embed-text:latest")

splitter = SemanticChunker(embeddings=embedding)

chunks = splitter.split_documents(documents)
for chunk in chunks:
    print("Chunks:",chunk.page_content)