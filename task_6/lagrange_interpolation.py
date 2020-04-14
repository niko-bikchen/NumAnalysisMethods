import numpy as np
from sympy import Symbol, lambdify, simplify
import math

# <Test data 1>
# x_values = np.array([0, 20, 40, 60, 80, 100], float)
# y_values = np.array([26.0, 48.6, 61.6, 71.2, 74.8, 75.2], float)
# </Test data 1>

# <Test data 2>
x_values = np.array([-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1], float)
# y_values = np.array([math.atan(2 * val) for val in x_values], float)
y_values = np.array([-1.570796327,
                     -0.848062079,
                     -0.5235987756,
                     -0.2526802551,
                     0,
                     0.2526802551,
                     0.5235987756,
                     0.848062079,
                     1.570796327])


# </Test data 2>


# <Main part>

def lagrange_interpolation(xp, xs, ys):
    return sum(yi * np.prod((xp - xs[xs != xi]) / (xi - xs[xs != xi])) for xi, yi in zip(xs, ys))


# UNCOMMENT LINES BELOW TO INPUT VALUES
# ! BE SURE TO COMMENT ALL TEST RELATED LINES

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

# </Main part>

# <Tests>

# Produces a polynomial, where you can plug 'x', from the 'polynomial' above
# Used for testing purposes
P = lambdify(x, polynomial)

# <Test set 1>
# print(f'For x = 0: {P(0)}')
# print(f'For x = 20: {P(20)}')
# print(f'For x = 100: {P(100)}')
# print(f'For x = 40: {P(40)}')
# </Test set 1>

# <Test set 2>
print(f'For x = -0.85: {P(-0.85)}')
print(f'For x = -0.35: {P(-0.35)}')
print(f'For x = 0.35: {P(0.35)}')
print(f'For x = 0.85: {P(0.85)}')
# </Test set 2>

# </Tests>
