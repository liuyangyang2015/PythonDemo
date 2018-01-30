def add(a,b):
    if(b==0):
        return a;
    sum=a^b;
    carry=(a&b)<<1;
    return add(sum,carry)

# print(str(add(3,-3)))
print('3')
add(3,-3)