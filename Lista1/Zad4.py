import numpy as np

transactionMatrix = np.array([[1,1,4], [1,2,1], [1,4,6], [2,1,6], [3, 4, 1], [3,2,2]])
itemMatrix = np.array([[1,2,0],[2,4,1], [3,6,1], [4,1,1]])

def checkMatrices(transactionMatrix, itemMatrix):
    print("\n", "-" * 10, "Pomyłki na paragonie", "-" * 10)
    for transaction in transactionMatrix:
        print("" if transaction[1] in itemMatrix.T[0] else "item not found\n", end="")
    for item in itemMatrix:
        print("" if item[2] in [0, 1] else "item type not in range\n", end="")
checkMatrices(transactionMatrix, itemMatrix)

def pearsonCheck(transactionMatrix, itemMatrix):
    print("\n", "-" * 10, "Łączna cena paragonu dla danej osoby", "-" * 10)
    itemCost = dict()
    for item in itemMatrix:
        itemCost[item[0]] = item[1]
    pearson = dict()
    for transaction in transactionMatrix:
        pearson[transaction[0]] = 0
    for transaction in transactionMatrix:
        pearson[transaction[0]] += transaction[2] * itemCost[transaction[1]]

    print(pearson)
pearsonCheck(transactionMatrix, itemMatrix)