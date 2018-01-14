import  numpy as np
# a = np.random.randn(4, 3) # a.shape = (4, 3)
# b = np.random.randn(3, 2) # b.shape = (3, 2)
# b = np.dot(a,b)
# print(b)
# # c = a*b

e= [1,2]
f= [1,2]
# print(e*f)
g= np.dot(e,f)
print(g)

# x=np.array(e)
# y=np.array(f)
# print(x)
# print(y)
# h=np.dot(x,y)
# print(h)
# print(x*y)

x=np.array(e).reshape(1,2)
y=np.array(f).reshape(1,2)
print(x)
print(y)
h=np.dot(x,y.T)
print(h)
print(x*y)

a = np.random.randn(3, 3)
print(a)
b = np.random.randn(3, 1)
print(b)
c = a*b
print(c)

