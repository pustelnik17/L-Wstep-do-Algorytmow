# Hubert Jackowski
import numpy as np

okFlag = True
class Client():
    def __init__(self, id, name=None, surname=None):
        self.data = dict()
        self.data["name"] = "NA"
        self.data["surname"] = "NA"

transactionMatrix = np.array([[0,0,4], [0,1,1], [0,3,6], [1,0,6], [2,3,1], [2,1,2]])
itemMatrix = np.array([[0,2,0],[1,4,1], [2,6,1], [3,1,1]])
VAT = 0.23
clients = []
for transaction in transactionMatrix:
    if transaction[0] not in clients:
        clients.append(Client(transaction[0]))
def setUpClients(clients):
    clients[0].data["name"] = "Michał"
    clients[0].data["surname"] = "Niski"
    clients[1].data["name"] = "Kuba"
    clients[1].data["surname"] = "Kowalski"
    clients[2].data["name"] = "Anna"
    clients[2].data["surname"] = "Kowalska"
setUpClients(clients)

def checkMatrices(transactionMatrix, itemMatrix):
    global okFlag
    print("\n", "-" * 10, "Pomyłki na paragonie", "-" * 10)
    for transaction in transactionMatrix:
        if transaction[1] not in itemMatrix.T[0]:
            okFlag = False
            print("item not found\n")
    for item in itemMatrix:
        if item[2] not in [0, 1]:
            okFlag = False
            print("item type not found\n")
    if okFlag == True:
        print("no issues with the data")
checkMatrices(transactionMatrix, itemMatrix)

def pearsonCheck(transactionMatrix, itemMatrix):
    print("\n", "-" * 10, "Łączna cena paragonu dla danej osoby", "-" * 10)
    if okFlag == False:
        print("error in data")
        return
    itemCost = dict()
    for item in itemMatrix:
        itemCost[item[0]] = item[1]
    pearson = dict()
    for transaction in transactionMatrix:
        pearson[transaction[0]] = 0
    for transaction in transactionMatrix:
        pearson[transaction[0]] += transaction[2] * itemCost[transaction[1]] * (1+VAT)
    for pearsonIndex in [*pearson]:
        print(clients[pearsonIndex].data["name"], clients[pearsonIndex].data["surname"], pearson[pearsonIndex])
pearsonCheck(transactionMatrix, itemMatrix)