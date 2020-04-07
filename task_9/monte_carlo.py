from scipy import random
import numpy as np
import matplotlib.pyplot as plt


def calculate_monte_carlo(a, b, f, n):
    """
    :parameter a - lower boundary
    :parameter b - upper boundary
    :parameter f - function to integrate
    :parameter n - number of points to evaluate
    """
    x_rand = random.uniform(a, b, n)
    integral = 0

    for i in range(n):
        integral += f(x_rand[i])

    return ((b - a) / n) * integral


N = 100000

print(calculate_monte_carlo(0, np.pi, np.sin, N))

answers = []

for _ in range(1000):
    answers.append(calculate_monte_carlo(0, np.pi, np.sin, N))

# Printing out first 5 answers
print(answers[0:5])

# Plotting distribution of the calculated area
plt.hist(answers, bins=30, ec='black')
plt.title('Calculated areas of distribution')
plt.xlabel('Areas')
plt.show()
