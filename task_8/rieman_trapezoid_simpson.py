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


print(f'Riemann: {calculate_riemann_sum(0, np.pi, np.sin, 20)}')
print(f'Trapezoid: {calculate_trapezoid_rule(0, np.pi, np.sin, 20)}')
print(f'Simpson: {calculate_simpson(0, np.pi, np.sin, 20)}')
