# 创建数据集
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

# 计算给定数据集的香农熵

from math import log
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] +=1
    shannonEnt = 0.0
    for key in labelCounts:
        print(labelCounts[key]/numEntries)
        prob = float(labelCounts[key]/numEntries)
        shannonEnt -= prob*log(prob,2)
    return shannonEnt

# 测试熵计算
def testCalcShannnonEnt(list):
    num = sum(list)
    shannonEnt = 0
    for entry in list:
        prop = entry/num
        shannonEnt -= prop*log(prop,2)
    return shannonEnt

