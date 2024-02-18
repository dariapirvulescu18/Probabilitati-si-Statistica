import math
import numpy as np
from matplotlib import pyplot as plt

# def chibrit(n,t,l):
#     d = np.random.uniform(0, t / 2,n)
#     teta = np.random.uniform(0, np.pi,n)
#     reusit= np.sum( d<=(l/2)*np.sin(teta))
#     #simulam grafic
#     rez = np.arange(1,n+1)/np.cumsum( d<=(l/2)*np.sin(teta))
#     plt.axhline(y=np.pi, color='red', linestyle='--', label='π')
#     plt.plot(np.arange(1,n+1),rez)
#     plt.show()
#     return reusit/n
#
# print('Probabilitatea: ',chibrit(100000,2,1))
#

# def throw_matches(num_matches, t,l):
#     cx = np.random.uniform(-10,10,num_matches)
#     cy = np.random.uniform(-(t/2),t/2,num_matches)
#     d = t/2-np.abs(cy)
#     teta = np.random.uniform(0, np.pi,num_matches)
#     #coordonate
#     x1 =cx + l / 2 * np.cos(teta)
#     y1 = cy + l / 2 * np.sin(teta)
#     x2 = cx- l / 2 * np.cos(teta)
#     y2 = cy - l / 2 * np.sin(teta)
#
#     plt.plot([-10, 10], [t / 2, t / 2], color='black')
#     plt.plot([-10, 10], [-t / 2, -t / 2], color='black')
#     plt.plot([-10, 10], [t / 2 + l / 2, t / 2 + l / 2], color='black')
#     plt.plot([-10, 10], [-t / 2 - l / 2, -t / 2 - l / 2], color='black')
#
#
#     culoare = {0: 'blue', 1: 'red'}
#
#     for i in range(num_matches):
#         if d[i] <= l / 2 * np.sin(teta[i]):
#             plt.plot([x1[i], x2[i]], [y1[i], y2[i]], color='red')
#         else:
#             plt.plot([x1[i], x2[i]], [y1[i], y2[i]], color='blue')
#
#     plt.plot()
#     plt.show()
#
#
# throw_matches(100, 2, 1)

def ex2_b(nr, lambd, n):
    sn = []
    for _ in range(0,nr):
        u = np.random.random(n)
        x = -np.log(u) / lambd
        sn.append(np.sum(x) / nr)
    plt.hist(sn,bins=30,density=True, edgecolor='black')
    plt.show()

ex2_b(100000, 0.5,100)