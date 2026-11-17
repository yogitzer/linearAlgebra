import numpy as np

np.set_printoptions(precision=4, suppress=True)

A = np.array([
    [0, 0, 0],
    [0, 2, 5],
    [0, 0, -1]
], dtype=float)

eig_A = np.linalg.eigvals(A).real

print("(1) A의 고유값 =")
print(eig_A)

B = np.array([
    [4, 0, 0],
    [0, 0, 0],
    [1, 0, -3]
], dtype=float)

eig_B = np.linalg.eigvals(B).real

print("\n(2) B의 고유값 =")
print(eig_B)