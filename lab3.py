import random
import matplotlib.pyplot as plt
import numpy as np

#metoda 1
def dau_cu_banul():
    a = np.random.random()
    if a < 0.5:
        return "cap"
    else:
        return "pajura"
def dau_cu_banul_masluit():
    a = np.random.random()
    if a < 0.75:
        return "cap"
    else:
        return "pajura"

def iterare_cinstita(num_aruncari):
    c = 0
    p = 0
    numere_curente = []  # Listă pentru a înregistra numărul de căderi cu cap la fiecare aruncare

    for i in range(num_aruncari):
        if dau_cu_banul() == "cap":
            c += 1
        else:
            p += 1
        numere_curente.append(c / (i + 1))

    return c, p, numere_curente
def iterare_masluita(num_aruncari):
    c = 0
    p = 0
    numere_curente = []  # Listă pentru a înregistra numărul de căderi cu cap la fiecare aruncare

    for i in range(num_aruncari):
        if dau_cu_banul_masluit() == "cap":
            c += 1
        else:
            p += 1
        numere_curente.append(c / (i + 1))

    return c, p, numere_curente

a, b, frecventa_caderilor_cu_cap_cinstit = iterare_cinstita(10000)
d, c, frecventa_caderilor_cu_cap_masluit = iterare_masluita(10000)
print("Se dau de", a, "ori cap\n")

def grafic_corect():
    num_experimente = np.arange(1, 10001)
    plt.plot(num_experimente, frecventa_caderilor_cu_cap_cinstit)
    plt.axhline(0.5, color='r', linestyle='--', label='50%')
    plt.xlabel('Numărul de aruncări')
    plt.ylabel('Frecvența căderilor cu capul în sus')
    plt.legend()
    plt.title('Simulare aruncare monedă')
    plt.show()
def grafic_masluit():
    num_experimente = np.arange(1, 10001)
    plt.plot(num_experimente, frecventa_caderilor_cu_cap_masluit)
    plt.axhline(0.5, color='r', linestyle='--', label='50%')
    plt.xlabel('Numărul de aruncări')
    plt.ylabel('Frecvența căderilor cu capul în sus')
    plt.legend()
    plt.title('Simulare aruncare monedă')
    plt.show()

# grafic_corect()
# grafic_masluit()
#metoda 2
def dau_cu_banul2():
    a = random.random()
    if a < 0.5:
        return "cap"
    else:
        return "pajura"

def iterare2(n):
    v=np.random.random(n)
    v=v<0.5
    return v


def grafic_corect2():
    num_experimente = np.arange(1, 10001)
    plt.plot(num_experimente,np.cumsum(iterare2(10000))/num_experimente )
    plt.axhline(0.5, color='r', linestyle='--', label='50%')
    plt.xlabel('Numărul de aruncări')
    plt.ylabel('Frecvența căderilor cu capul în sus')
    plt.legend()
    plt.title('Simulare aruncare monedă')
    plt.show()
grafic_corect2()
