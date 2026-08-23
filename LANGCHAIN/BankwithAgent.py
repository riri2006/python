from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from bln import current
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")
memory = MemorySaver()

balance =  current()
@tool
def withdraw(amount : int):
    if(amount > balance):
        return"INSUFFICIENT BALANCE"
    else:
        balance -= amount
        return "WITHDRAWN SUCCESSFULLY"

agent = create_agent(
    model= llm,
    checkpointer= memory,
    tools=[withdraw]
)
config = {"configurable": {"thread_id":"1"}}

# while True:
#     query = input("YOU: ")
#     if query in ["exit","terminate","quit"]:
