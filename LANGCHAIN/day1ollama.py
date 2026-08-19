from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3.2:latest")

user = input("Please ask your question: ")
data = llm.invoke(user)

print(data.content)
