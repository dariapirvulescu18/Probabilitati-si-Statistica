import math
import random


def k_optim(n, k):
    prim = k / n
    suma = 0
    for i in range(k, n):
        suma += 1/i
    return prim * suma

def case(n, k):
    caz_fav = 0
    for i in range(0, 100000):
        vec = [i for i in range(1, n + 1)]
        random.shuffle(vec)
        primele_k = vec[:k]
        vec = vec[k:]
        minim = min(primele_k)
        for ales in vec:
            if ales < minim:
                if ales == 1:
                    caz_fav += 1
                break
    return caz_fav / 100000

n = 50
max = 0
k = 0
for i in range(1, n - 1):
   rez = k_optim(n, i)
   if rez > max:
      max = rez
      k = i
print(f"Pentru n = {n}, k simulat este {k}, iar n/e = {n / math.e}")
print(case(n, k))

