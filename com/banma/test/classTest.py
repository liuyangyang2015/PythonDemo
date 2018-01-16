class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

    def __init__(self):
        self.data = []
        self.name= 'hihi'

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

print(MyClass.i)
print( MyClass.f)
x = MyClass()
print( x.i)
x.i =3
print( MyClass.i)
print( x.i)
MyClass.i =333
y = MyClass()
print( MyClass.i)
print( x.i)
print( y.i)
print( y.data)
print(y.name)
print(MyClass.i)
print(y.__class__)
from math import pi, sin

sine_table = {x: sin(x * pi / 180) for x in range(0, 91)}
print(sine_table)

# unique_words = set(word  for line in page  for word in line.split())
# print(unique_words)