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
def withdraw(amount : str):
    global balance
    
    """WITHDRAW MONEY FROM BANK ACCOUNT """
    if(amount > balance):
        return"INSUFFICIENT BALANCE"
    else:
        balance -= amount
        return "WITHDRAWN SUCCESSFULLY"

@tool
def current_balance():
    """Shows current balance of user"""
    return balance

agent = create_agent(
    model= llm,
    checkpointer= memory,
    tools=[withdraw, current_balance]
)
config = {"configurable": {"thread_id":"1"}}

while True:
    query = input("YOU: ")
    if query in ["exit","terminate","quit"]:
        print("TERMINATING CONVERSATION..THNAK YOU")
        break
    response = agent.invoke({
        "messages":[{"role":"user", "content":query}]
    }, config= config)

    print("Assistant: ",response['messages'][-1].content)
