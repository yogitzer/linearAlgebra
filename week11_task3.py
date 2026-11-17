import numpy as np

A = np.array([
    [3, -1, -1],
    [-12, 0, 5],
    [4, -2, -1]
], dtype=float)

eigenvalues, X = np.linalg.eig(A)

order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

lamda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

print("X =")
print(X)
print("\nlamda =")
print(lamda)