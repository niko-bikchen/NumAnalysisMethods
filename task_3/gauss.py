import numpy as np

a = np.array([
    [0, 1],
    [1, 0]
], float)

b = np.array([1, 1], float)

n = len(b)

x = np.zeros(n, float)


def gauss(a: np.array, b: np.array, x: np.array) -> np.array:
    for i in range(0, n):
        max_el = abs(a[i][i])
        max_row = i

        for k in range(i + 1, n):
            if abs(a[k][i]) > max_el:
                max_el = abs(a[k][i])
                max_row = k

        for k in range(i, n):
            temp = a[max_row][k]
            a[max_row][k] = a[i][k]
            a[i][k] = temp

        for k in range(0, n - 1):
            for i in range(k + 1, n):
                if a[i, k] == 0:
                    continue
                else:
                    factor = a[k, k] / a[i, k]

                    for j in range(k, n):
                        a[i, j] = a[k, j] - a[i, j] * factor

                    b[i] = b[k] - b[i] * factor

    x[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        sum_as = 0
        for j in range(i + 1, n):
            sum_as += a[i, j] * x[j]
        x[i] = (b[i] - sum_as) / a[i, i]

    return x


# print("Enter matrix size: ")
# n = int(input('> '))
#
# matrix = []
# row = []
# b = []
#
# for i in range(n):
#     for j in range(n):
#         print(f"Enter value for the a[{i}, {j}]")
#         el = float(input('> '))
#         row.append(el)
#     matrix.append(row.copy())
#     row.clear()
#
#     print(f"Enter value for the b[{i}]")
#     b_el = float(input('> '))
#     b.append(b_el)
#
# a = np.array(matrix, float)
# b = np.array(b, float)
# x = np.zeros(n, float)

print(gauss(a, b, x))
