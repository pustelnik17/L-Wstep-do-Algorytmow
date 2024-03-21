# Hubert Jackowski
import copy
import random
import matplotlib.pyplot as plt
import numpy


class Office:
    def __init__(self, a=0, b=0, c=0, e=0):
        self.posts = dict()
        self.postsNumberOfClients = dict()
        self.posts["a"] = [0 for _ in range(a)]
        self.posts["b"] = [0 for _ in range(b)]
        self.posts["c"] = [0 for _ in range(c)]
        self.posts["e"] = [0 for _ in range(e)]
        self.postsNumberOfClients["a"] = [0 for _ in range(a)]
        self.postsNumberOfClients["b"] = [0 for _ in range(b)]
        self.postsNumberOfClients["c"] = [0 for _ in range(c)]
        self.postsNumberOfClients["e"] = [0 for _ in range(e)]

    def passCycle(self):
        for taskType in ["a", "b", "c", "e"]:
            for i in range(len(self.posts[taskType])):
                self.posts[taskType][i] -= 1

    def giveTasks(self, customerQueue):
        for taskType in ["a", "b", "c"]:
            for i in range(len(self.posts[taskType])):
                if self.posts[taskType][i] == -1:
                    self.posts[taskType][i] = customerQueue.getByType(taskType)
                    self.postsNumberOfClients[taskType][i] += 1
        for i in range(len(self.posts["e"])):
            if self.posts["e"][i] == -1:
                self.posts["e"][i] = customerQueue.pop(0)
                self.postsNumberOfClients["e"][i] += 1

    def giveTasksOptimised(self, customerQueue):
        taskMeter = {"a": 0, "b": 0, "c": 0}
        for taskType in ["a", "b", "c"]:
            for i in range(len(self.posts[taskType])):
                if self.posts[taskType][i] == -1:
                    self.posts[taskType][i] = customerQueue.getByType(taskType)
                    self.postsNumberOfClients[taskType][i] += 1
            for i in range(customerQueue.size()):
                taskMeter[customerQueue.type[i]] += 1

        for i in range(len(self.posts["e"])):
            if self.posts["e"][i] == -1:
                self.posts["e"][i] = customerQueue.getByType(max(taskMeter, key=taskMeter.get))
                self.postsNumberOfClients["e"][i] += 1

    def getProgress(self):
        for taskType in ["a", "b", "c", "e"]:
            print("|", taskType, ": ", sep='', end='')
            for i in range(len(self.posts[taskType])):
                print(self.posts[taskType][i], " ", end="")
        print()

    def finished(self):
        for taskType in ["a", "b", "c", "e"]:
            for i in range(len(self.posts[taskType])):
                if self.posts[taskType][i] > 0:
                    return False
        return True

    def getNumberOfClients(self):
        for taskType in ["a", "b", "c", "e"]:
            print("|", taskType, ": ", sep='', end='')
            for i in range(len(self.postsNumberOfClients[taskType])):
                print(self.postsNumberOfClients[taskType][i], " ", end="")
        print()

class CustomerQueue:
    def __init__(self, n):
        self.type = [random.choice(["a", "b", "c"]) for _ in range(n)]
        self.complexity = []
        for i in range(len(self.type)):
            if self.type[i] == "a":
                self.complexity.append(random.randint(1, 4))
            elif self.type[i] == "b":
                self.complexity.append(random.randint(5, 8))
            elif self.type[i] == "c":
                self.complexity.append(random.randint(9, 12))

    def size(self):
        return len(self.type)

    def pop(self, i=0):
        if len(self.type) == 0:
            return 0
        self.type.pop(i)
        result = self.complexity.pop(i)
        return result

    def getByType(self, taskType):
        for i in range(len(self.type)):
            if self.type[i] == taskType:
                return self.pop(i)
        return 0

    def bubbleSort1(self):
        LEN = self.size()
        for i in range(LEN):
            for j in range(0, LEN - 1):
                if self.complexity[j] > self.complexity[j + 1]:
                    temp = self.complexity[j]
                    self.complexity[j] = self.complexity[j + 1]
                    self.complexity[j + 1] = temp
                    temp = self.type[j]
                    self.type[j] = self.type[j + 1]
                    self.type[j + 1] = temp
        return

    def bubbleSort2(self):
        LEN = self.size()
        for i in range(LEN):
            for j in range(0, LEN - 1):
                if self.complexity[j] < self.complexity[j + 1]:
                    temp = self.complexity[j]
                    self.complexity[j] = self.complexity[j + 1]
                    self.complexity[j + 1] = temp
                    temp = self.type[j]
                    self.type[j] = self.type[j + 1]
                    self.type[j + 1] = temp
        return


def standardModel(office, customerQueue):
    print("-"*10, "Standardowy Model", "-"*10)
    numberOfIterations = 0
    while True:
        office.passCycle()
        office.giveTasks(customerQueue=customerQueue)
        # office.getProgress()
        numberOfIterations += 1
        if customerQueue.size() == 0 and office.finished():
            break
    print("Number of iterations: ", numberOfIterations)


def firstQueueCheck():
    print("-"*20, "1. Trzy Urzedy", "-"*20)
    customerQueue = CustomerQueue(30)
    standardModel(Office(3, 3, 3), copy.deepcopy(customerQueue))
    standardModel(Office(2, 2, 2, 3), copy.deepcopy(customerQueue))
    standardModel(Office(1, 2, 3, 1), copy.deepcopy(customerQueue))


firstQueueCheck()


def modifiedModel(office, customerQueue):
    numberOfIterations = 0
    while True:
        office.passCycle()
        office.giveTasks(customerQueue=customerQueue)
        numberOfIterations += 1
        if customerQueue.size() == 0 and office.finished():
            break
    return numberOfIterations


def secondQueueCheck():
    print("-" * 20, "2. Trzy Urzedy", "-" * 20)
    modelTimes = [[], [], []]
    for queueIter in range(100):
        customerQueue = CustomerQueue(40)
        modelTimes[0].append(modifiedModel(Office(3, 3, 3), copy.deepcopy(customerQueue)))
        modelTimes[1].append(modifiedModel(Office(2, 2, 2, 3), copy.deepcopy(customerQueue)))
        modelTimes[2].append(modifiedModel(Office(1, 2, 3, 1), copy.deepcopy(customerQueue)))
    plt.hist(modelTimes[0], color="yellow", label="3A,3B,3C")
    plt.hist(modelTimes[1], color="red", label="2A,2B,2C,3E")
    plt.hist(modelTimes[2], color="orange", label="1A,2B,3C,1E")
    plt.legend()
    plt.show()


secondQueueCheck()


def sortedTest():
    print("-" * 20, "3. Trzy Urzedy", "-" * 20)
    customerQueue = CustomerQueue(30)
    customerQueue1 = copy.deepcopy(customerQueue)
    customerQueue2 = copy.deepcopy(customerQueue)
    customerQueue1.bubbleSort1()
    customerQueue2.bubbleSort2()
    print("-" * 20, "rosnąco", "-" * 20)
    standardModel(Office(3, 3, 3), copy.deepcopy(customerQueue1))
    standardModel(Office(2, 2, 2, 3), copy.deepcopy(customerQueue1))
    standardModel(Office(1, 2, 3, 1), copy.deepcopy(customerQueue1))
    print("-" * 20, "malejaco", "-" * 20)
    standardModel(Office(3, 3, 3), copy.deepcopy(customerQueue2))
    standardModel(Office(2, 2, 2, 3), copy.deepcopy(customerQueue2))
    standardModel(Office(1, 2, 3, 1), copy.deepcopy(customerQueue2))


sortedTest()