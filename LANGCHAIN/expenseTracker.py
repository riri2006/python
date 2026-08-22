from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")
memory = MemorySaver()

expense = []
@tool
def add_expense(spent:str, category:str):
    """Adding expense category wise"""
    expense.append({
        "amount spent" : spent,
        "category": category
    })

@tool
def show_expense():
    """show the expense"""
    return expense

agent = create_agent(
    model= llm,
    checkpointer= memory,
    tools= [add_expense, show_expense]
)

config = {"configurable": {"thread_id":"1"}}

while True:
    query = input("You: ")
    if query in ["exit", "quit", "terminate"]:
        print("TERMINATING CONVERSATION.. THANK YOU AND HAVE A NICE DAY..")
        break

    response = agent.invoke({
        "messages":[{"role":"user", "content":query}]
    }, config= config)

    print("Assistant: ", response['messages'][-1].content)