import random
import copy
import operator

def popSort(alist):
    for i in range(len(alist) - 1):
        for j in range(len(alist) - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist

def generateRandomArry(maxSize,maxValue):
    size=int((maxSize+1)*random.random())
    print(size)
    arr=[]
    for i in range(size):
        arr.append(int(maxValue*random.random()))
    return arr

def Tester():
    testTime=10
    maxSize=50
    maxValue=50
    succeed=True
    for i in range(testTime):
        arr1=generateRandomArry(maxSize,maxValue)
        arr2=copy.deepcopy(arr1)
        arr1=sorted(arr1)
        arr2=popSort(arr2)
        if (not operator.eq(arr1,arr2)):
            succeed=False
            print(succeed)
            print(arr1)
            print(arr2)
            return
    print(succeed)
    return
