import math as m
from typing import Callable

functions: dict = {
    'sqrt(x+9) + 1': lambda x: m.sqrt(x + 9) + 1,
    'e^x + 1 - sqrt(9 - x^2)': lambda x: m.exp(x) + 1 - m.sqrt(9 - x ** 2)
}


def fixed_point_iteration(func: Callable[[float], float],
                          x_0: float,
                          eps: float) -> float:
    x: float = x_0

    while abs(x - func(x)) > eps:
        x = func(x)

    return x


func_tups = list(zip(range(0, len(functions.keys())), functions.keys()))

print('Pick a function number: ', func_tups)
func_num = int(input('> '))
func = func_tups[func_num][1]
print('Enter x_0')
x_0 = float(input('> '))
print('Enter precision')
eps = float(input('> '))

print(f'Solution for "{func}" is: {fixed_point_iteration(functions[func], x_0, eps)}')

# print(fixed_point_iteration(functions['sqrt(x+9) + 1'], 4, 0.0000001))
# print(fixed_point_iteration(functions['e^x + 1 - sqrt(9 - x^2)'], 0.5, 0.0000001))
