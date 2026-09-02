from pydantic import BaseModel, StrictInt
from typing import Optional

#Int me "" string dala still it typcasted that as int
class Student(BaseModel):
    name: str
    age: int
student = Student(name="Riddhi", age="20")
print(student)

