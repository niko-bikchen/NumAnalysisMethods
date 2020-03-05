import numpy as np


def tdma(a, b, c, d):
    num_f = len(d)
    a_cp, b_cp, c_cp, d_cp = map(np.array, [a, b, c, d])

    for i in range(1, num_f):
        w = a_cp[i - 1] / b_cp[i - 1]
        b_cp[i] = b_cp[i] - w * c_cp[i - 1]
        d_cp[i] = d_cp[i] - w * d_cp[i - 1]

    x_cp = b_cp
    x_cp[-1] = d_cp[-1] / b_cp[-1]

    for i in range(num_f - 2, -1, -1):
        x_cp[i] = (d_cp[i] - c_cp[i] * x_cp[i + 1]) / b_cp[i]

    return x_cp


a = np.array([3., 1, 3])  # a_1 is 0 by definition
b = np.array([10., 10., 7., 4.])
c = np.array([2., 4., 5.])  # c_3 is 0 by definition
d = np.array([3, 4, 5, 6.])

print(tdma(a, b, c, d))
