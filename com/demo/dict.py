di = {1: 13, 2: 34,3:45}
# print(di)
# for key , value in di.items():
#     print(key,value)
#
# for key in di:
#     print(key)

# for value in di.values():
#     print(value)
# for i in range(3):
#         print(i)
#         if i == 1:
#             continue
#             print("s")
#         elif i==2:
#             print("am")
#         else:
# pass
#             pass



# def name_the_benefits_of_functions():
#     list_of_benefits = list_benefits(a)
#     for benefit in list_of_benefits:
#         print(build_sentence(benefit))
#
# def build_sentence(benefit):
#     pass
#
# def list_benefits(a):
#     # pass
#     return "More organized code ", "More readable code "
#
# a=2
# a = name_the_benefits_of_functions()

class MyClass:
    var = "hello"

    def say(a,b):
        print("hello"+str(a)+b)
    def __call__(self, *args, **kwargs):
        print("is called")
#
x = MyClass()
# x.say("world")
#
# a=callable(x)
# print(a)
# x()
# print(callable(MyClass))

from enum import Enum ,unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(type(Weekday.Sun))
print(Weekday['Sun'].value)
print(Weekday.Sun.value)
print(Weekday(1))
print(type(MyClass))
print(type(x))

def fn(self, name='world'): # 先定义函数
     print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn))
h =Hello()
print(type(Hello))
print(type(h))
a=Hello
print(type(a))
print(type(a()))

a = {1: 10, 2: 20, 3: 30}
a=[1,2,3,'sd']
for key , value in enumerate(a):
    print(key,value)

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
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

print("==============")
a=33
try:
    # if a ==3:
        raise IndexError
except IndexError as ie:
    print('*********')
else:
    print('nnnnnnnnnnnnnnn')
finally:
    print('jjjjjjjjjjjjjjjjjjj')

print('********************')
for i in reversed(range(10)) :
    print(i)