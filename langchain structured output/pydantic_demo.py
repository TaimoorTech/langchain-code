from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Taimoor" # set default val
    age: Optional[int] = None # if no age then val none
    email: EmailStr # can validate email
    cgpa: float = Field(ge=0, le=10, description="This number represent cgpa of student") # constraints
    # description tells llm what to do

# as name is str, so in twill give error this is beenfit of pydantic
# new_student = {'name': 32}

# In Python, type coercion (commonly referred to as implicit type conversion) is the process where the language automatically changes a value from one data type to another during an operation. Likr in this as age is int but giving number in int provide as int in outpt and pydantic does it itself
new_student = {'name': 'taimoor', 'age': '32', 'email': 'abc@yahoo.com', 'cgpa': 9}

# pydantic object
student = Student(**new_student)

# converting pydantic obj into dict
student_dict = dict(student)

print(student_dict['age'])

# converting pydantic obj into json
student_json = student.model_dump_json()