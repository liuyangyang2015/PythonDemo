from com.banma.foo import bar
m = (bar)
print("hie")
from com.banma.test import fibo
a= fibo.fib2(11)
print(a)
from . import fibo
# from .. foo import bar


from com.banma.demo import test


a = 'Hello, world.'
print(str(a))
print(repr(a))

for x in range(1, 11):
    print(repr(x).ljust(2), repr(x * x).ljust(3), end=' ')
     # Note use of 'end' on previous line
    print(repr(x * x * x).ljust(4))
# This is a test
# This is a test
# [1, "simple", "list"]This is a test
[1, "simple", "list"]