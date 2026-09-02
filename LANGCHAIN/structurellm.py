from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

class Person(BaseModel):
    name: str = Field(
        description="Person's name",
        min_length=2,
        max_length=20
    )

    age: int = Field(
        description="Person's age"
    )

model = ChatGroq(
    model="openai/gpt-oss-20b"
)

strmodel = model.with_structured_output(Person)

user = input("ASK: ")
response = strmodel.invoke(user)

print("DIRECT: ", response)


print("Name:", response.name)
print("Age:", response.age)