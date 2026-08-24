from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

schedule =[]

class Assistant :
    def __init__(self,name,ai):
        self.name= name
        self.ai = ai

    def agent(self):
        llm = ChatGroq(model="openai/gpt-oss-20b")
        memory = MemorySaver()
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
            query = input(f"{self.name}: ")
            if query in ["quit", "terminate", "exit"]:
                print("TERMINATING THE CONVERSATION.. THANK YOU AND HAVE A GOOD DAY")
                break

            response =  agent.invoke({
                "messages":[{"role":"user", "content":query}]
            }, config=configuration)

            print(f"{self.ai}: ", response['messages'][-1].content)

user = input("Enter your name: ")
ai = input("What do you want to call your study assistant? ")
a1 = Assistant(user, ai)
a1.agent()

