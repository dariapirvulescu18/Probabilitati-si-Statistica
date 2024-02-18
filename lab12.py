import math
import numpy as np
from matplotlib import pyplot as plt
nr_simulari = int(1/(12 * 0.05 * 10**(-6)))
def ex1(n):
    verfica = 0
    for _ in range (1,101):
        val = np.random.random(n)
        val = np.sin(val)
        val = np.sum(val)/n
        if abs(val -(1-np.cos(1))) < 0.001:
            verfica = verfica+1
    return verfica

print(ex1(nr_simulari))
print(ex1(20000))


def f(t):
    return np.sin(2 * t) + 0.3 * np.cos(10 * t) + 0.05 * np.sin(100 * t)

def p_sigma2(s, sigma_squared):
    return np.exp(-0.5 * (s / np.sqrt(sigma_squared))**2) / np.sqrt(2 * np.pi * sigma_squared)


def ex2(t_values, sigma_squared, n=10000):
    transformed_signal = np.zeros_like(t_values)

    for _ in range(n):
        s_samples = np.random.normal(0, np.sqrt(sigma_squared), len(t_values))
        integral_contributions = f(t_values - s_samples) * p_sigma2(s_samples, sigma_squared)
        transformed_signal += integral_contributions

    transformed_signal /= n
    return transformed_signal


t_values = np.linspace(0, 5, 500)


sigma_squared = 0.1

transformed_signal = ex2(t_values, sigma_squared)

plt.figure(figsize=(10, 6))
plt.plot(t_values, f(t_values), label='Original Signal')
plt.plot(t_values, transformed_signal, label=f'Transformed Signal (σ² = {sigma_squared})')
plt.title('Monte Carlo Simulation of Transformed Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
