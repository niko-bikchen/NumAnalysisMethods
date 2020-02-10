import math as m
from typing import Callable, List


def bisection(func: Callable[[float], float],
              rng: List[float],
              eps: float) -> float:
    a: float = rng.pop(0)
    b: float = rng.pop(0)

    c: float = 0

    while abs(b - a) / 2.0 > eps:
        c = (a + b) / 2.0

        if m.isclose(func(c), 0.0):
            return c
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c

    return c


functions: dict = {
    'sin(x)': lambda x: m.sin(x),
    'cos(x)': lambda x: m.cos(x),
    'sin(x) - x': lambda x: m.sin(x) - x,
    'log(x) - 1': lambda x: m.log(x) - 1,
    'e^x - 2 + x': lambda x: m.exp(x) - 2 + x,
    'x^2 + 10x - 3': lambda x: x ** 2 + 10 * x - 3,
    '10 + 6x - x^2': lambda x: 10 + 6 * x - x ** 2
}

func_tups = list(zip(range(0, len(functions.keys())), functions.keys()))

print('Pick a function number: ', func_tups)
func_num = int(input('> '))
func = func_tups[func_num][1]
print('Enter left range bound')
a = float(input('> '))
print('Enter right range bound')
b = float(input('> '))
print('Enter precision')
eps = float(input('> '))

print(f'Solution for "{func}" is: {bisection(functions[func], [a, b], eps)}')

# print(bisection(functions['sin(x) - x'], [-1, 1], 0.000000001))
# print(bisection(functions['sin(x)'], [m.pi - 1, m.pi], 0.000000001))
# print(bisection(functions['log(x) - 1'], [2, 3], 0.000000001))
# print(bisection(functions['e^x - 2 + x'], [0, 2], 0.000000001))
print(bisection(functions['x^2 + 10x - 3'], [-5, 5], 0.000000001))
# print(bisection(functions['10 + 6x - x^2'], [-5, 5], 0.000000001))
