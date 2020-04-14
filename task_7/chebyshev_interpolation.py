import numpy as np
from sympy import Symbol, lambdify, simplify


def cheb_poli(degree, x):
    if degree == 0:
        return 1
    if degree == 1:
        return x
    else:
        return 2 * x * cheb_poli(degree - 1, x) - cheb_poli(degree - 2, x)


def a_sum(n, f, k):
    return sum(
        [
            f(
                np.cos(
                    (2 * j + 1) * np.pi / (2 * n + 2)
                )
            )
            *
            np.cos(
                k * (2 * j + 1) * np.pi / (2 * n + 2)
            )
            for j in range(0, n + 1)
        ]
    )


def custom_a_sum(n, values, k):
    return sum(
        [
            val
            *
            np.cos(
                k * (2 * j + 1) * np.pi / (2 * n + 2)
            )
            for j, val in enumerate(values)
        ]
    )


def chebyshev_interpolation(n, f, x):
    summa = 0

    for i in range(1, n + 1):
        summa += 2 * a_sum(n, f, i) * cheb_poli(i, x)

    return summa / (n + 1)


def custom_chebyshev_interpolation(n, values, x):
    summa = 0

    for i in range(0, n + 1):
        if i == 0:
            summa += custom_a_sum(n, values, i) * cheb_poli(i, x)
        else:
            summa += 2 * custom_a_sum(n, values, i) * cheb_poli(i, x)

    return summa / (n + 1)


f_values = [1.396263402,
            1.047197552,
            0.6981317006,
            0.3490658498,
            0,
            -0.3490658498,
            -0.6981317006,
            -1.047197552,
            -1.396263402]
# f_values = [1.1009971305064690925,
#             1.0471975511965977461,
#             0.90970073709819939446,
#             0.59993424850586212036,
#             0,
#             -0.59993424850586212036,
#             -0.90970073709819939446,
#             -1.0471975511965977461,
#             -1.1009971305064690925]
num = len(f_values)

# UNCOMMENT LINES BELOW TO INPUT NODE VALUES BY HAND
# f_values = []
# num = int(input('Number of nodes: '))
#
# for i in range(num):
#     f_values.append(float(input(f'Enter value of function in node number {i}: ')))
#
x_val = Symbol('x')
polinomial = simplify(custom_chebyshev_interpolation(num - 1, f_values, x_val))
print(polinomial)

# x_val = Symbol('x')
# polinomial = simplify(chebyshev_interpolation(8, lambda arg: cos(arg), x_val))
# print(polinomial)

P = lambdify(x_val, polinomial)
print(f'Chebyshev polinomial for -0.85: {P(-0.85)}')
print(f'Chebyshev polinomial for -0.35: {P(-0.35)}')
print(f'Chebyshev polinomial for 0.35: {P(0.35)}')
print(f'Chebyshev polinomial for 0.85: {P(0.85)}')
# print(f'Chebyshev polinomial for -0.9: {P(-0.9)}')
# print(f'Chebyshev polinomial for -0.3: {P(-0.3)}')
# print(f'Chebyshev polinomial for 0.3: {P(0.3)}')
# print(f'Chebyshev polinomial for 0.9: {P(0.9)}')
