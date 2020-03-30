import numpy as np
from sympy import Symbol, lambdify, simplify
from math import cos, pi, atan


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
                cos(
                    (((2 * j) + 1) * pi) / ((2 * n) + 2)
                )
            )
            *
            cos(
                (k * ((2 * j) + 1) * pi) / ((2 * n) + 2)
            )
            for j in range(0, n + 1)
        ]
    )


def custom_a_sum(n, values, k):
    return sum(
        [
            val
            *
            cos(
                (k * ((2 * j) + 1) * pi) / ((2 * n) + 2)
            )
            for j, val in enumerate(values)
        ]
    )


def chebyshev_interpolation(n, f, x):
    summa = 0

    for i in range(1, n + 1):

        if i == 1:
            summa += ((a_sum(n, f, 1) * cheb_poli(1, x)) / (n + 1))
        else:
            summa += ((2 * a_sum(n, f, i) * cheb_poli(i, x)) / (n + 1))

    return summa


def custom_chebyshev_interpolation(n, values, x):
    summa = 0

    for i in range(1, n + 1):

        if i == 1:
            summa += ((custom_a_sum(n, values, 1) * cheb_poli(1, x)) / (n + 1))
        else:
            summa += ((2 * custom_a_sum(n, values, 1) * cheb_poli(i, x)) / (n + 1))

    return summa


# f_values = []
# num = int(input('Number of nodes: '))
#
# for i in range(num):
#     f_values.append(float(input(f'Enter value of function in node number {i}: ')))
#
# x_val = Symbol('x')
# polinomial = simplify(custom_chebyshev_interpolation(num, f_values, x_val))
# print(polinomial)

x_val = Symbol('x')
# x_val = -0.9
polinomial = simplify(chebyshev_interpolation(9, lambda arg: atan(arg * 2), x_val))
print(polinomial)

# x_val = Symbol('x')
# polinomial = simplify(cheb_poli(6, x_val))
# print(polinomial)
