from com.algorithm import decisionTree
dataSet,labels = decisionTree.createDataSet()
print(dataSet)
print(labels)

shannonEnt = decisionTree.calcShannonEnt(dataSet)
print(shannonEnt)

test = decisionTree.testCalcShannnonEnt([3,3])
test2 = decisionTree.testCalcShannnonEnt([2,4])
test3 = decisionTree.testCalcShannnonEnt([1,1,4])
print(test,":",test2,":",test3)

from pylab import *

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plot(X,C)
plot(X,S)

show()