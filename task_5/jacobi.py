import numpy as np


def jacobi(matrix, b, n, x=None):
    if x is None:
        x = np.zeros(matrix[0])

    matrix_d = np.diag(matrix)
    matrix_r = matrix - np.diagflat(matrix_d)

    for i in range(n):
        x = (b - np.dot(matrix_r, x)) / matrix_d

    return x


matrix = np.array([[2.0, 1.0], [5.0, 7.0]], float)
b = np.array([11.0, 13.0], float)
init_guess = np.array([1.0, 1.0], float)

print(jacobi(matrix, b, 25, init_guess))
