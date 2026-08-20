from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-20b")

memory = []

while True:
    query = input("ASK: ")

    if query in ["exit", "terminate"]:
        break

    memory.append({
        "role" : "user",
        "content" : query
    })

    response = llm.invoke(memory)

    print("AI RESPONSE: ", response.content)

    memory.append({
        "role" : "assistant",
        "content" : response.content
    })