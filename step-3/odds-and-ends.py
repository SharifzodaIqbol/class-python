from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int
jhon = Employee('jhon','computer lab',1000)

print(jhon.dept)

print()

print(jhon.salary)