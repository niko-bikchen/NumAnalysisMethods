from typing import Callable


def newtons_method(f: Callable[[float], float],
                   df: Callable[[float], float],
                   x_0: float,
                   eps: float) -> float:
    x: float = x_0

    while abs(f(x)) > eps:
        x = x - (f(x) / df(x))

    return x


functions: dict = {
    'x^3 - x^2 - 1': {
        'f': lambda x: x ** 3 - x ** 2 - 1,
        'df': lambda x: 3 * x ** 2 - 2 * x
    },
    'x^3 - 3*x^2 - 1': {
        'f': lambda x: x ** 3 - 3 * x ** 2 - 1,
        'df': lambda x: 3 * x ** 2 - 6 * x
    }
}

func_tups = list(zip(range(0, len(functions.keys())), functions.keys()))

print('Pick a function number: ', func_tups)
func_num = int(input('> '))
func = func_tups[func_num][1]
print('Enter x_0')
x_0 = float(input('> '))
print('Enter precision')
eps = float(input('> '))

print(f'Solution for "{func}" is: {newtons_method(functions[func]["f"], functions[func]["df"], x_0, eps)}')

print(newtons_method(functions['x^3 - x^2 - 1']['f'], functions['x^3 - x^2 - 1']['df'], 1, 0.000000001))
