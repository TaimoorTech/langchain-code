from typing import TypedDict

# Define a TypedDict for a person with name and age fields
class Person(TypedDict):
    name: str
    age: int


# Create an instance of the Person TypedDict
new_person: Person = {
    "name": "Alice",  
    "age": 30,
 }

print(new_person)
