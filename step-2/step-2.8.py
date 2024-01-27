class Bag:
    def __init__(self):
        self.data = []

    def add(self, x: str):
        self.data.append(x)

    def addtwice(self, x: str):
        self.add(x)
        self.add(x)

    def remove_add(self,x: str):
        if x in self.data:
            self.data.remove(x)
        else:
           raise ValueError("Error")

x = Bag()
value = x.add("Hello World")
print(*x.data,end=" ")
x.remove_add(
    "Hello World"
)
print()
dif = x.addtwice("True")
print(*x.data,end=" ")

#Hello World
#True True