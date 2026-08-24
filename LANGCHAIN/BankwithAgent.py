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

pinn = "1234"
@tool
def withdraw(amount : str, pin:str):
    """WITHDRAW MONEY FROM BANK ACCOUNT """

    global balance
    if(pin==pinn):
        if(int(amount) > balance):
            return"INSUFFICIENT BALANCE"
        else:
            balance -= int(amount)
            return "WITHDRAWN SUCCESSFULLY"
    else:
        return "invalid credentials"

@tool
def current_balance(pin:str):
    """Shows current balance of user after checking whetere the pin is matching or not"""
    if (pin==pinn):
        return balance
    else :
        return "INVALID CREDENTIALS"

@tool
def Deposit(amount:str, pin:str):
    """Deposits money in bank account"""
    global balance 
    if (pin == pinn):
        balance += int(amount)
        return "Deposited successfully"
    else: 
        return "invalid credentials"
        
    




agent = create_agent(
    model= llm,
    checkpointer= memory,
    tools=[withdraw, current_balance, Deposit]
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
