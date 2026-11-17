import numpy as np

A = np.array([
    [2, 3],
    [3, -6]
], dtype=float)

char_poly = np.poly(A)

eigenvalues = np.linalg.eigvals(A)
eigenvalues = np.sort(eigenvalues)

np.set_printoptions(precision=4, suppress=True)

print("특성다항식 계수 (poly(A)) =")
print(char_poly)

print("\n고유값 (eig(A)) =")
print(eigenvalues)
