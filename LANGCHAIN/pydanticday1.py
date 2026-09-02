from pydantic import BaseModel, StrictInt
from typing import Optional

#Int me "" string dala still it typcasted that as int
class Student(BaseModel):
    name: str
    age: int
student = Student(name="Riddhi", age="20")
print(student)

##strictInt 
class Fruit(BaseModel):
    name: str
    units: StrictInt
fruit1 = Fruit(name="Mango", units=100)
print(fruit1)
try:
    fruit2 = Fruit(name="Lychee", units="100")
    print(fruit2)
except :
    print("Invalid data type")

#optional
class Employee(BaseModel):
    name: str
    age: int
    salary: Optional[float] = None

emp1 = Employee(name="Riddhi", age=20, salary=95000)
emp2 = Employee(name="Kashish", age=25)
print(emp1)
print(emp2)