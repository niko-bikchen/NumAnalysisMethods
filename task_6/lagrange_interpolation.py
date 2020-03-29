import numpy as np
from sympy import Symbol, lambdify, simplify
import math


def lagrange_interpolation(xp, xs, ys):
    return sum(yi * np.prod((xp - xs[xs != xi]) / (xi - xs[xs != xi])) for xi, yi in zip(xs, ys))


# Test set 1
# x_values = np.array([0, 20, 40, 60, 80, 100], float)
# y_values = np.array([26.0, 48.6, 61.6, 71.2, 74.8, 75.2], float)

# Test set 2
x_values = np.array([-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1], float)
y_values = np.array([math.atan(2 * val) for val in x_values], float)

# num = int(input('Number of points: '))
#
# x_values = np.zeros(num)
# y_values = np.zeros(num)
#
# for i in range(num):
#     x_values[i] = float(input(f'Enter value for x{i}: '))
#     y_values[i] = float(input(f'Enter value for y{i}: '))

x = Symbol('x')
polynomial = simplify(lagrange_interpolation(x, x_values, y_values))
print(polynomial)

# For tests
P = lambdify(x, polynomial)

# For test set 1
# print(f'For x = 0: {P(0)}')
# print(f'For x = 20: {P(20)}')
# print(f'For x = 100: {P(100)}')
# print(f'For x = 40: {P(40)}')

# For test set 2
print(f'For x = -0.9: {P(-0.9)}')
print(f'For x = -0.3: {P(-0.3)}')
print(f'For x = 0.3: {P(0.3)}')
print(f'For x = 0.9: {P(0.9)}')
