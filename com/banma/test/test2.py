# f=open('test1.py','r')
# a=f.name
# b=f.read()
# print(f)
# print(a)
# print(b)
# print(f.closed)
# f.close()
# print(f.closed)
# f=open('test1.py','a')
# f.write('This is a test\n')

import json
f=open('test1.py','r+')
x=[1, 'simple', 'list']
# json.dump(x, f)

x = json.load(f)
print(x)