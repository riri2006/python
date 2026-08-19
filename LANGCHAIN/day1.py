from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
llm = ChatGroq(model = "openai/gpt-oss-20b")

while True :
    user = input("please ask your question: ")
    data = llm.invoke(user)
    print(data.content)

    