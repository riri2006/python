from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain.tools import tool

llm = ChatGroq(model = "openai/gpt-oss-20b")
memory = MemorySaver()

@tool
def add (a:int,b:int):
    """Addition of two numbers"""
    return a+b

@tool
def sub (a:int, b:int):
    """Subtraction of numbers"""
    return a-b

@tool
def mul (a:int,b:int):
    """Multiplication of two numbers"""
    return a*b

@tool
def div (a:int, b:int):
    """Division of numbers"""
    try:
        return a/b
    except ZeroDivisionError:
        return "Cant dvide by 0"


agent = create_agent(
    model = llm,
    checkpointer= memory,
    tools= [add, sub, mul, div ]

)
config = { "configurable" : { "thread_id" : "1"}}

while True:
    query = input("Ask your question: ")
    if query in ["terminate", "exit", "quit"]:
        print("Terminating the conversation..thank u")
        break
    response = agent.invoke({
        "messages":[{"role": "user", "content": query }]
    },config = config)

    print("AI: ",response['messages'][-1].content)