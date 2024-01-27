class Reverse:
    """Итератор для перебора последовательности в обратном направлении."""
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')

for char in rev:
    print(char,end="")

