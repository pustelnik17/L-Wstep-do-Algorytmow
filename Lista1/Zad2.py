# Hubert Jackowski
import numpy as np
L, M = 5, 5
p = np.random.randint(low = 1, high = 10, size=(L, M))
q = np.random.randint(low = 1, high = 10, size=(L, M))
print(p)
print(q)
def symmetricalDistance(p, q):
    print("\n", "-" * 10, "Odległość symetryczna macierzy", "-" * 10)
    result = 0
    for rowIndex in range(L):
        for colIndex in range(M):
            result += np.absolute(p[rowIndex, colIndex] - q[rowIndex, colIndex])
    print(result)
symmetricalDistance(p, q)