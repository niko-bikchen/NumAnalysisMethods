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


print(fixed_point_iteration(functions['sqrt(x+9) + 1'], 4, 0.0000001))
print(fixed_point_iteration(functions['e^x + 1 - sqrt(9 - x^2)'], 0.5, 0.0000001))
