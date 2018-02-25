import numpy as np
from  com.algorithm import kNN
data=[[1,1.1],[1,1],[0,0],[0,0.1]]
dataSet=np.array(data)
labels=['A','A','B','B']
result=kNN.classify0([0,0],dataSet,labels,3)
print(result)
