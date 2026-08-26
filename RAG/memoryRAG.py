from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings 
from langchain_chroma import Chroma 
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(model="openai/gpt-oss-20b")
memory = MemorySaver()
agent = create_agent(
    model= llm,
    checkpointer= memory
)


doc = PyPDFLoader("Roads_to_Mussoorie.pdf")
data = doc.load()

splitter =  RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 100
)

chunk = splitter.split_documents(data)

embedding = OllamaEmbeddings( model="nomic-embed-text:latest")

vdb = Chroma.from_documents(
    documents=chunk,
    embedding=embedding,
    persist_directory="./rk_db"
)

while True:
    query = input("Ask: ")
    if query in ["exit", "terminate"]:
        print("Terminating... Thank youuu")
        break

    result = vdb.similarity_search(
        query= query,
        k=3
    )

    context = "\n\n".join(
    doc.page_content
    for doc in result
    )

    prompt = f"""
    You are an assistant that answers questions about the PDF.

    Use the PDF context below to answer questions about the book.

    PDF context:
    {context}

    Current question:
    {query}

    You can also use previous conversation messages when the user asks about
    something discussed earlier in this conversation.

    If the answer is not available in the PDF and it was not discussed earlier,
    say:
    "I could not find this information."
    """


    response = agent.invoke({
        "messages":[{"role":"user", "content": prompt}]
    },config={"configurable":{"thread_id":"1"}})

    print("\nAnswer:")
    print(response['messages'][-1].content)
    print()
