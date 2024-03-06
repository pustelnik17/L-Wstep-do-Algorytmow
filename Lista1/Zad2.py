import numpy as np
L, M = 5, 2
p = np.random.randint(low = 1, high = 10, size=(L, M))
q = np.random.randint(low = 1, high = 10, size=(L, M))
print(p, q)

def symmetricalDistance(p, q):
    result = 0
    for rowIndex in range(L):
        for colIndex in range(M):
            result += np.absolute(p[rowIndex, colIndex] - q[rowIndex, colIndex])
    print(result)
symmetricalDistance(p, q)