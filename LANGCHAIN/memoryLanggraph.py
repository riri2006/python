from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

llm = ChatGroq(model="openai/gpt-oss-20b")
memory = MemorySaver()

agents = create_agent(
    model = llm,
    checkpointer= memory
)

config = {
    "configurable": {"thread_id": "1"}
}

while True: 
    query = input("You: ")

    if query in ["terminate", "quit", "exit"]:
        print("TERMINATING THE CONVERSATION.. THANKUU MWAHHH")
        break

    response = agents.invoke({
        "messages": [{
            "role" : "user",
            "content" : query
        }]
    }, config=config)

    print("Your Assistant: ",response['messages'][-1].content)
