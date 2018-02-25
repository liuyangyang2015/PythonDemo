import numpy as np
import operator
from imp import reload
# k近邻算法实现

# data=[[1,1.1],[1,1],[0,0],[0,0.1]]
# dataSet=np.array(data)
# labels=['A','A','B','B']

def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances=sqDiffMat.sum(axis=1)
    distance = sqDistances**0.5
    sortedDistIndicies = np.argsort(distance)
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
    sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse =True)
    return sortedClassCount[0][0]

# reload(np)
