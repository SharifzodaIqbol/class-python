with open('myfile.txt','w') as file:
    file.write("Hello world!!!")

for element in [1, 2, 3]:
    print(element, end=" ") # 1 2 3

print()

for element in (1, 2, 3):
    print(element, end=" ") # 1 2 3

print()

for key in {'one' : 1, 'two' : 2}:
    print(key, end=" ") # one two

print()

for char in "123": # 1 2 3
    print(char, end=" ")

print()

for line in open("myfile.txt"):
    print(line, end=" ") # Hello world!!!