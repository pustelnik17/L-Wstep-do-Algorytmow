# Hubert Jackowski
import numpy as np
def generateList(n):
    return [np.random.randint(0, high=9) for i in range(n)]
def bubbleSort(LST):
    result = LST.copy()
    LEN = len(result)
    for i in range(LEN):
        for j in range(0, LEN - 1):
            if (result[j] > result[j + 1]):
                temp = result[j]
                result[j] = result[j + 1]
                result[j + 1] = temp
    return result
def insertionSort(LST):
    result = LST.copy()
    for i in range(len(result)):
        for j in range(0, i):
            if (result[i] < result[j]):
                temp = result[i]
                result[i] = result[j]
                result[j] = temp
    return result
def selectionSort(LST):
    result = LST.copy()
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if (result[i] > result[j]):
                temp = result[i]
                result[i] = result[j]
                result[j] = temp
    return result

LST = generateList(10)
print(LST, bubbleSort(LST), insertionSort(LST), selectionSort(LST))