import numpy as np

transactionMatrix = np.array([[0,0,4], [0,1,1], [0,3,6], [1,0,6], [2,3,1], [2,1,2]])
itemMatrix = np.array([[0,2,0],[1,4,1], [2,6,1], [3,1,1]])
VAT = 0.23
clientData = [dict(), dict(), dict()]
def setUpClients():
    clientData[0]["name"] = "Michał"
    clientData[0]["surname"] = "Niski"
    clientData[1]["name"] = "Kuba"
    clientData[1]["surname"] = "Kowalski"
    clientData[2]["name"] = "Anna"
    clientData[2]["surname"] = "Kowalska"
setUpClients()

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
        pearson[transaction[0]] += transaction[2] * itemCost[transaction[1]] * (1+VAT)
    for pearsonIndex in [*pearson]:
        print(clientData[pearsonIndex]["name"], clientData[pearsonIndex]["surname"], pearson[pearsonIndex])
pearsonCheck(transactionMatrix, itemMatrix)