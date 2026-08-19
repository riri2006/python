from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-20b")

memory = [] #empty list hoti to store past data memory as a notebook

while True:
    query = input("Ask :")


    memory.append({
        "role" : "user",
        "content" : query
    })

    response = llm.invoke(memory) #memory as a notebook taki past data aur context k liye samajh aaye assistant ko

    print("ASSISTANT: ", response.content)

    memory.append({
        "role" : "assistant",
        "content" : response.content
    })

