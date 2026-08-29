#-------------------------------------recursive chunk example-----------------------------------------------------

# from langchain_community.document_loaders import Docx2txtLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# data = Docx2txtLoader("testing.docx")
# documents= data.load()

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size = 7,
#     chunk_overlap=1
# )
# chunks = splitter.split_documents(documents)
# for chunk in chunks:
#     print("Chunks:",chunk.page_content)


#---------------------------------semantic chunks example---------------------------------------------------------
from llama_parse import LlamaParse
from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
load_dotenv()
import os

parser = LlamaParse(
    api_key=os.getenv("LLAMA_API_KEY"),
    result_type="markdown"
)
path = input("Enter path: ")
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
    print(chunk)