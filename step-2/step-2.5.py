class Dog:

    kind = 'canine'

    def __init__(self,name):
        self.name = name
d = Dog('Fido')
e = Dog('Buddy')
print(f'порода {d.kind}, имя {d.name}') #first dog: порода canine, имя Fido
print(f'порода {e.kind}, имя {e.name}') #second dog: порода canine, имя Buddy

