import numpy as np
import matplotlib.pyplot as plt
import numpy.random
import math


def ploteaza(l) :
    u = numpy.random.uniform(0.0, 1.0, 10000)
    t = -1/l * np.log(1-u)
    plt.hist(t, bins=30, density=True, color='g')
    xgraf = np.linspace(0, max(t), 100)
    ex = l * np.exp(-l * xgraf)
    plt.plot(xgraf, ex)
    plt.show()

def Cauchy(x0, gamma):
    u = numpy.random.uniform(0.0, 1.0, 10000)
    t = x0 + gamma * np.tan(np.pi * (u - 0.5))
    plt.hist(t, bins=30, range = [-10, 10], density=True, color='g')
    xgraf = np.linspace(-10, 10, 100)
    ex = 1 / (np.pi * gamma * (1 + ((xgraf - x0) / gamma) ** 2))
    plt.plot(xgraf, ex)
    plt.show()


# ploteaza(5)
Cauchy(1,1)