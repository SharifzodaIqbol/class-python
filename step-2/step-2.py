class Complex:
    """Простой Класс"""
    def __init__(self,realpart: float,imgpart: float):
        self.r = realpart
        self.i = imgpart
x = Complex(3.0, -4.5)
print(x.i,x.r,end=" ")
#     -4.5 3.0
