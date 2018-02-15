import numpy as np
np.ones((3,4))

# film demo
list = [(3,104),(2,100),(1,81),(101,10),(99,5),(98,2),(18,90)]
print(list)

for key , value in list:
    a = (key-18)**2+(value-90)**2
    print(np.sqrt(a))