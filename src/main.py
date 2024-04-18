from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

x0 = 1
xk = 3
h1 = 0.5
h2 = 0.25
value = 0.257531


def f(x):
    return sqrt(x) / (4 * x + 3)


def rectangle_method(h):
    integral = 0
    n = np.arange(x0, xk, h)
    for i in n:
        integral += f(i) * h
    return integral


def trapezoidal_method(h):
    integral = (f(x0) + f(xk))
    n = np.arange(x0, xk, h)
    for i in n[1:]:
        integral += 2 * f(i)
    return integral * h / 2


def simpson_method(h):
    integral = (f(x0) + f(xk))
    n = np.arange(x0, xk, h)
    for i in range(1, len(n)):
        if i % 2 == 1:
            integral += 4 * f(n[i])
        else:
            integral += 2 * f(n[i])
    return integral * h / 3


def runge(h1, h2, p):
    result = h2 - (h2 - h1) / (2 ** p - 1)
    print("Runge checking result is " + str(result) + ", Absolute error " + str(abs(result - value)))


def plot():
    plt.grid(True)
    x = np.linspace(1, 3, 10 ** 5)
    y = [f(i) for i in x]
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    print("Result with step 0.5")
    print("Rectangle method:", rectangle_method(h1))
    print("Trapezoidal method:", trapezoidal_method(h1))
    print("Simpson method:", simpson_method(h1))
    print()
    print("Result with step 0.25")
    print("Rectangle method:", rectangle_method(h2))
    print("Trapezoidal method:", trapezoidal_method(h2))
    print("Simpson method:", simpson_method(h2))
    print()
    print("Runge checking")
    runge(rectangle_method(h1), rectangle_method(h2), 1)
    runge(trapezoidal_method(h1), trapezoidal_method(h2), 2)
    runge(simpson_method(h1), simpson_method(h2), 4)
    plot()
