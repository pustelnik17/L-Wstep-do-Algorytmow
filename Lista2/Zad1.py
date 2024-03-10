# Hubert Jackowski
import time

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
def checkExecutionTime(function, arg):
    start = time.perf_counter_ns()
    function(arg)
    return time.perf_counter_ns() - start

def avgAndMaxExecutionTime():
    print("-"*10, "średni i maksymalny (z dziesięciu przebiegów) czas działania poszczególnych algotrytmów sortowania", "-"*10)
    times = {"bubbleSort": [], "insertionSort": [], "selectionSort": []}
    for i in range(10):
        lst = generateList(1000)
        times["bubbleSort"].append(checkExecutionTime(bubbleSort, lst))
        times["insertionSort"].append(checkExecutionTime(insertionSort, lst))
        times["selectionSort"].append(checkExecutionTime(selectionSort, lst))
    print(f"bubbleSort: avg: {np.average(times["bubbleSort"])}ns max: {max(times["bubbleSort"])}ns")
    print(f"insertionSort: avg: {np.average(times["insertionSort"])}ns max: {max(times["insertionSort"])}ns")
    print(f"selectionSort: avg: {np.average(times["selectionSort"])}ns max: {max(times["selectionSort"])}ns")
avgAndMaxExecutionTime()