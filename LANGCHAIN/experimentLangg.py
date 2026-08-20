
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

class Assitant:
    def __init__(self, name, ai):
        self.name = name
        self.ai = ai

    def assistant(self):

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
            query = input(f"{self.name}:   ")

            if query in ["terminate", "quit", "exit"]:
                print("TERMINATING THE CONVERSATION.. THANKUU MWAHHH")
                break

            response = agents.invoke({
                "messages": [{
                    "role" : "user",
                    "content" : query
                }]
            }, config=config)

            print(f"{self.ai}:  ",response['messages'][-1].content)


name = input("WHAT DO WE CALL YOU??: ")
ai = input("WHAT DO YOU WANT TO CALL YOUR ASSISTANT??: " )
print()
a1 = Assitant(name, ai)
a1.assistant()



