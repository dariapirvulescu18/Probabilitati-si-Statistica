import random
import numpy as np
def joc(n,usi):
    castig_stat = 0
    castig_schimb = 0
    lista_usi=[i for i in range (1,usi+1)]
    for _ in range(n):

        initial = random.randint(1, usi)

        masina = random.randint(1, usi)

        if(initial==masina):
            castig_stat += 1
        else:
            castig_schimb+=1


    return castig_stat, castig_schimb

num_simulations = 10000
usi=10
x, y = joc(num_simulations, usi)

print(f"Probabilitatea de câștig rămânând la alegerea inițială: {x / num_simulations }")
print(f"Probabilitatea de câștig schimbând alegerea: {y / num_simulations }")
