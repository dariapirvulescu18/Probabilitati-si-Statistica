import math

import numpy as np
from matplotlib import pyplot as plt
nr_simulari=1000000
def Bernoulli(n, p ):
    variabila=np.random.random(n)
    variabila= (variabila<p).astype(int)
    bins=[-0.5,0.5,1.5]
    plt.hist(variabila, bins=bins, ec="pink",density=True)
    plt.title("Bernoulli")
    plt.xticks([0,1])
    plt.show()

Bernoulli(nr_simulari,0.8)

def Binomiala(n,p):
    nr=np.random.random((nr_simulari,n))
    nr=np.sum(nr<p,axis=1)
    plt.hist(nr, bins=np.arange(0,n+2), ec="pink", density=True)
    plt.title("Binomiala")
    plt.xticks(np.arange(0,n+2))
    plt.show()


Binomiala(20,1/20)

def Geometric(p):
    nr = np.random.random(nr_simulari)
    variabila = np.floor(np.log(nr) / np.log(1 - p)).astype(int)
    bins = np.arange(0, np.max(variabila) + 2) - 0.5
    plt.hist(variabila, bins=bins, ec="pink", density=True)
    plt.title("Geometrica")
    plt.xticks(np.arange(0, np.max(variabila) + 1))
    plt.show()

Geometric(0.5)

def ex3(p,x):
    n=np.cumsum(p)

n = 65643291 * (97 ** 146)
m= 4000000 *(100 **146)
print(n/m)

def Poisson(lamb):
    vec = vector(lamb)
    bins = np.arange(0, max(vec) + 2) - 0.5
    plt.hist(vec, bins=bins,  density=True, ec="pink")
    plt.title("Poisson")
    plt.xticks(np.arange(0, max(vec) + 1))
    plt.show()

def vector(lamb):
    vec = []
    for _ in range(100000):
        k = 0
        numar = np.random.random()
        F = np.exp(-lamb)
        while numar >= F:
            F += np.exp(-lamb) * lamb ** k / math.factorial(k)
            k += 1
        vec.append(k)
    return np.array(vec)

Poisson(1)

def Hypergeometrica(N,K,n):
    vec = np.random.random(size=(10000, n))
    good = K / N
    vec = np.sum(vec < good, axis=1)
    start = -0.5
    bins = [start]
    for i in range(1, K + 2):
        start += 1
        bins.append(start)
    plt.hist(vec, bins=bins,  density=True, ec="pink")
    plt.title("hypergeometrica")
    plt.xticks(np.arange(0, K+2))
    plt.show()

Hypergeometrica(50,15,7)