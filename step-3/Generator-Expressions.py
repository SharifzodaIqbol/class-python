from dataclasses import dataclass

print(sum(i*i for i in range(10))) # 285

x = [10, 20, 30]
y = [7, 5, 3]
print(sum(x*y for x,y in zip(x,y))) # 260

page = ['hello', 'hello', 'dir', 'del', 'hello']
unique_word = set(word for line in page for word in line.split())
print(unique_word) # 'dir', 'del', 'hello'

@dataclass
class Student:
    age: int
    gpa: int

data = 'yield'
print(list(data[i] for i in range(len(data)-1, -1, -1))) #['d', 'l', 'e', 'i', 'y']