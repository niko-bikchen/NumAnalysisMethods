import numpy as np


def calculate_riemann_sum(a, b, f, n, mode='mid'):
    """
    :parameter a - lower boundary
    :parameter b - upper boundary
    :parameter f - function to integrate
    :parameter n - number of segments
    :parameter mode - method to use for integral calculation
    """
    section_length = (b - a) / n
    xs = np.linspace(a, b, n + 1)

    if mode == 'mid':
        xs_mid = (xs[:-1] + xs[1:]) / 2
        return np.sum(f(xs_mid) * section_length)
    elif mode == 'left':
        xs_left = xs[:-1]
        return np.sum(f(xs_left) * section_length)
    elif mode == 'right':
        xs_right = xs[1:]
        return np.sum(f(xs_right) * section_length)
    else:
        return None


def calculate_trapezoid_rule(a, b, f, n):
    """
    :parameter a - lower boundary
    :parameter b - upper boundary
    :parameter f - function to integrate
    :parameter n - number of segments
    """
    section_length = (b - a) / n
    xs = np.linspace(a, b, n + 1)
    ys = f(xs)
    ys_right = ys[1:]
    ys_left = ys[:-1]
    return (section_length / 2) * np.sum(ys_right + ys_left)


def calculate_simpson(a, b, f, n):
    """
    :parameter a - lower boundary
    :parameter b - upper boundary
    :parameter f - function to integrate
    :parameter n - number of segments
    """
    if n % 2 == 1:
        return None
    else:
        section_length = (b - a) / n
        xs = np.linspace(a, b, n + 1)
        ys = f(xs)
        return (section_length / 3) * np.sum(ys[0:-1:2] + 4 * ys[1::2] + ys[2::2])


def calculate_error(m, a, b, n, mode):
    h = (b - a) / n

    if mode == 'riemann':
        return max(m) * h ** 2 * (b - a) / 24
    elif mode == 'trapezoid':
        return max(m) * h ** 2 * (b - a) / 12
    elif mode == 'simpson':
        return max(m) * h ** 4 * (b - a) / 2880


functions = [
    lambda x: np.cos(x),
    lambda x: np.sin(x),
    lambda x: 2 * x ** 2,
    lambda x: np.cos(3 * x / 2)
]

riemann = calculate_riemann_sum(np.pi / 3, 2 * np.pi / 3, functions[3], 10)
trapezoid = calculate_trapezoid_rule(np.pi / 3, 2 * np.pi / 3, functions[3], 10)
simpson = calculate_simpson(np.pi / 3, 2 * np.pi / 3, functions[3], 10)

print(f'Riemann: {riemann}')
print(f'Trapezoid: {trapezoid}')
print(f'Simpson: {simpson}\n')

print(f'Riemann theoretical error: {calculate_error([0, 9 / 4], np.pi / 3, 2 * np.pi / 3, 10, "riemann")}')
print(
    f'Trapezoid theoretical error: {calculate_error([0, 9 / 4], np.pi / 3, 2 * np.pi / 3, 10, "trapezoid")}')
print(f'Simpson theoretical error: {calculate_error([0, 81 / 16], np.pi / 3, 2 * np.pi / 3, 10, "simpson")}\n')

print(f'Riemann real error: {np.abs((-2 / 3) - riemann)}')
print(f'Trapezoid real error: {np.abs((-2 / 3) - trapezoid)}')
print(f'Simpson real error: {np.abs((-2 / 3) - simpson)}')
