from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model= "openai/gpt-oss-20b")
memory = MemorySaver()

recipe=[]
@tool
def add_recipe(dish:str, ingredients:str, steps:str):
    """give recipe and steps for the dish user asked and store it """
    recipe.append(
        {
            "dish" : dish,
            "ingredients": ingredients,
            "steps": steps
        }
    )
    return "recipe added successfully"


agent = create_agent(
    model= llm,
    checkpointer= memory,
    tools=[add_recipe]
)

config = {"configurable":{"thread_id":"1"}}

while True:
    query = input("You: ")
    if query in ["exit", "terminate", "quit"]:
        print("TERMINATING CONVERSATION.. THANK YOUU")
        break

    response = agent.invoke(
        {
            "messages":[{"role": "user", "content": query}]
        }, config=config
    )

    print("Assistant: ", response["messages"][-1].content)