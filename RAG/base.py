from pydantic import BaseModel

class Address(BaseModel):
    city: str
    pincode: int


class Student(BaseModel):
    name: str
    age: int
    address: Address

student = Student(
    name="Riddhi",
    age=21,
    address={
        "city":"Mumbai",
        "pincode":401501
    }
)

print(student)