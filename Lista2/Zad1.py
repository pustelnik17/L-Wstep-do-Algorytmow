# Hubert Jackowski
import math
import time
import numpy as np
import matplotlib.pyplot as plt

class Sort:
    @staticmethod
    def generateList(n, low=0, high=9):
        return [np.random.randint(low, high=high) for _ in range(n)]

    @staticmethod
    def bubbleSortBreak(LST):
        result = LST.copy()
        LEN = len(result)
        for i in range(LEN):
            swapFlag = False
            for j in range(0, LEN - 1):
                if result[j] > result[j + 1]:
                    temp = result[j]
                    result[j] = result[j + 1]
                    result[j + 1] = temp
                    swapFlag = True
            if not swapFlag:
                return result
        return result

    @staticmethod
    def bubbleSortShort(LST):
        result = LST.copy()
        LEN = len(result)
        for i in range(LEN):
            for j in range(0, LEN - 1):
                if result[j] > result[j + 1]:
                    temp = result[j]
                    result[j] = result[j + 1]
                    result[j + 1] = temp
        return result

    @staticmethod
    def bubbleSort(LST):
        result = LST.copy()
        LEN = len(result)
        for i in range(LEN):
            for j in range(0, LEN - 1):
                if result[j] > result[j + 1]:
                    temp = result[j]
                    result[j] = result[j + 1]
                    result[j + 1] = temp
        return result

    @staticmethod
    def insertionSort(LST):
        result = LST.copy()
        for i in range(len(result)):
            for j in range(0, i):
                if result[i] < result[j]:
                    temp = result[i]
                    result[i] = result[j]
                    result[j] = temp
        return result

    @staticmethod
    def selectionSort(LST):
        result = LST.copy()
        for i in range(len(result)):
            for j in range(i + 1, len(result)):
                if result[i] > result[j]:
                    temp = result[i]
                    result[i] = result[j]
                    result[j] = temp
        return result

    @staticmethod
    def checkExecutionTime(function, arg):
        start = time.perf_counter_ns()
        function(arg)
        return time.perf_counter_ns() - start

def avgAndMaxExecutionTime():
    print("-"*10, "średni i maksymalny (z dziesięciu przebiegów) czas działania poszczególnych algotrytmów sortowania", "-"*10)
    exectionTimes = {"bubbleSort": [], "insertionSort": [], "selectionSort": []}
    for i in range(10):
        lst = Sort.generateList(1000)
        exectionTimes["bubbleSort"].append(Sort.checkExecutionTime(Sort.bubbleSort, lst))
        exectionTimes["insertionSort"].append(Sort.checkExecutionTime(Sort.insertionSort, lst))
        exectionTimes["selectionSort"].append(Sort.checkExecutionTime(Sort.selectionSort, lst))
    print(f"bubbleSort: avg: {np.average(exectionTimes['bubbleSort'])}ns max: {max(exectionTimes['bubbleSort'])}ns")
    print(f"insertionSort: avg: {np.average(exectionTimes['insertionSort'])}ns max: {max(exectionTimes['insertionSort'])}ns")
    print(f"selectionSort: avg: {np.average(exectionTimes['selectionSort'])}ns max: {max(exectionTimes['selectionSort'])}ns")
avgAndMaxExecutionTime()

def plotExecuitonTimes():
    print("-"*10, "średnie i maksymalne czasy działania poszczególnych algorytmów dla długości ciągów", "-"*10)
    tempDict = {10: [], 20: [], 50: [], 100: [], 200: [], 500: [], 1000: []}
    exectionTimes = {"bubbleSort": tempDict, "insertionSort": tempDict, "selectionSort": tempDict}
    for listSize in [10, 20, 50, 100, 200, 500, 1000]:
        for j in range(10):
            lst = Sort.generateList(listSize)
            exectionTimes["bubbleSort"][listSize].append(Sort.checkExecutionTime(Sort.bubbleSort, lst))
            exectionTimes["insertionSort"][listSize].append(Sort.checkExecutionTime(Sort.insertionSort, lst))
            exectionTimes["selectionSort"][listSize].append(Sort.checkExecutionTime(Sort.selectionSort, lst))
    for sortingAlgorithm in ["bubbleSort", "insertionSort", "selectionSort"]:
        f = plt.plot([*exectionTimes[sortingAlgorithm].keys()], [np.average(element) for element in exectionTimes[sortingAlgorithm].values()], label="avg", color="green", marker='o')
        f = plt.plot([*exectionTimes[sortingAlgorithm].keys()], [max(element) for element in exectionTimes[sortingAlgorithm].values()], label="max", color="red", marker='o')
        plt.xlim(0, 1000)
        plt.title(sortingAlgorithm)
        plt.xlabel("length of list(#)")
        plt.ylabel("time(ns)")
        plt.legend()
        plt.show()
plotExecuitonTimes()

def modifiedBubbleSortComparison():
    print("-"*10, "czasy działania wszystkich trzech wersji implementacyjnych algorytmu sortowania bąbelkowego", "-"*10)
    lst = Sort.generateList(1000)
    print("bubbleSort", Sort.checkExecutionTime(Sort.bubbleSort, lst), "ns")
    print("bubbleSortBreak", Sort.checkExecutionTime(Sort.bubbleSortBreak, lst), "ns")
    print("bubbleSortShort", Sort.checkExecutionTime(Sort.bubbleSortShort, lst), "ns")
modifiedBubbleSortComparison()

def executionTests():
    print("-"*10, "testy wydajnościowe: n/t(n) | (n · log(n))/t(n)", "-"*10)
    for n in [10, 100, 1000]:
        lst = Sort.generateList(n)
        print(f"n={n}")
        for algorithm in [Sort.bubbleSort, Sort.insertionSort, Sort.selectionSort]:
            time = Sort.checkExecutionTime(algorithm, lst)
            print(algorithm.__name__, "n/t(n): ", n / time, "#/ns   |  (n · log(n))/t(n)", (n * math.log2(n)) / time, " |  (n^2)/t(n)",n**2 / time)
executionTests()