from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

llm = ChatGroq(model="openai/gpt-oss-20b")
memory = MemorySaver()
schedule =[]

@tool
def add_schedule(hours: str, subject:str):
    """Add the hours and work to do"""
    schedule.append({
        "hours": hours,
        "subject": subject
    })
    return "Added to schedule.." 

@tool
def show_schedule():
    """show the schedule.."""
    return schedule

agent = create_agent(
    model = llm,
    checkpointer= memory,
    tools=[add_schedule, show_schedule]
)

configuration = {"configurable":{"thread_id":"1"}}

while True:
    query = input("You: ")
    if query in ["quit", "terminate", "exit"]:
        print("TERMINATING THE CONVERSATION.. THANK YOU AND HAVE A GOOD DAY")
        break

    response =  agent.invoke({
        "messages":[{"role":"user", "content":query}]
    }, config=configuration)

    print("Study Partner: ", response['messages'][-1].content)