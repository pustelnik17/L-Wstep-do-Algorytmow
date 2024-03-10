# Hubert Jackowski
import numpy as np
from scipy.linalg import lu

n = 5
matrix = np.random.randint(low = 1, high = 10, size=(n, n+1))
p, l, upperStairMatrix = lu(matrix)
print(matrix)
print("\n", "-" * 10, "Postać schodkowa zredukowana", "-" * 10)
print(upperStairMatrix)