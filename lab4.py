import random
import time
import matplotlib.pyplot as plt
import numpy as np

def R_vs_V_nevectorizat(n):
    zar_rosu =[2,2,2,5,5,5]
    zar_verde=[3,3,3,3,3,6]
    pv=0;
    pr=0;
    for i in range(1,n+1):
        rosu = random.choice(zar_rosu)
        verde = random.choice(zar_verde)
        if rosu <verde:
            pv=pv+1
        else:
            pr=pr+1
    if pv>pr:
        print("Zarul verde este mai bun ca zarul rosu, probabilitatea este ", pv/n, "mai mare ca pr", pr/n)
    else:
        print("Zarul rosu este mai bun ca zarul verde, probabilitatea este ", pr/n, "mai mare ca pv", pv/n)

def R_vs_V_vectorizat(n):
    zar_rosu = np.array([2, 2, 2, 5, 5, 5])
    zar_verde = np.array([3, 3, 3, 3, 3, 6])
    lansari_rosu = np.random.choice(zar_rosu, n)
    lansari_verde = np.random.choice(zar_verde, n)
    castigate_verde = np.sum(lansari_rosu < lansari_verde)
    castigate_rosu = n - castigate_verde

    if castigate_verde > castigate_rosu:
        print("Zarul verde este mai bun ca zarul rosu, probabilitatea este", castigate_verde / n, "mai mare ca pr",
              castigate_rosu / n)
    else:
        print("Zarul rosu este mai bun ca zarul verde, probabilitatea este", castigate_rosu / n, "mai mare ca pv",
              castigate_verde / n)


def R_vs_V_vs_N_vectorizat(n):
    zar_rosu = np.array([2, 2, 2, 5, 5, 5])
    zar_verde = np.array([3, 3, 3, 3, 3, 6])
    zar_negru = np.array([1,4,4,4,4,4])
    lansari_rosu = np.random.choice(zar_rosu, n)
    lansari_verde = np.random.choice(zar_verde, n)
    lansari_negru =np.random.choice(zar_negru,n)
    castigate_verde = np.sum((lansari_rosu < lansari_verde) & (lansari_negru<lansari_verde))
    castigate_rosu = np.sum((lansari_rosu > lansari_negru) & (lansari_rosu > lansari_verde))
    castiga_negru = np.sum ((lansari_negru >lansari_verde) & (lansari_negru >lansari_rosu))
    if castiga_negru>castigate_rosu and castiga_negru >castigate_verde:
        print("negru castiga")
    if(castigate_rosu > castigate_verde and castigate_rosu >castiga_negru):
        print("rosu castiga")
    if(castigate_verde > castigate_rosu and castigate_verde > castiga_negru):
        print("verde castiga")
    return castigate_rosu/n, castigate_verde /n, castiga_negru/n

timp_inceput=time.time()
R_vs_V_nevectorizat(1000000)
timp_sfarsit=time.time()
timp_executie = timp_sfarsit - timp_inceput
print(f"Timpul de executie al functiei nevectorizate: {timp_executie} secunde")

timp_inceput=time.time()
R_vs_V_vectorizat(1000000)
timp_sfarsit=time.time()
timp_executie = timp_sfarsit - timp_inceput
print(f"Timpul de executie al functiei vectorizate: {timp_executie} secunde")

R_vs_V_vs_N_vectorizat(10000)

def grafic():
    # Numărul de lansări
    numar_lansari = 100

    rezultate_rosu = []
    rezultate_verde = []
    rezultate_negru = []

    for i in range(1, numar_lansari + 1):
        prob_rosu, prob_verde, prob_negru = R_vs_V_vs_N_vectorizat(i)
        rezultate_rosu.append(prob_rosu)
        rezultate_verde.append(prob_verde)
        rezultate_negru.append(prob_negru)

    # Crearea graficului
    plt.plot(range(1, numar_lansari + 1), rezultate_rosu, label="Zar Rosu", color="red")
    plt.plot(range(1, numar_lansari + 1), rezultate_verde, label="Zar Verde", color ="green")
    plt.plot(range(1, numar_lansari + 1), rezultate_negru, label="Zar Negru", color ="black")

    # Etichete și legendă
    plt.xlabel("Numarul de Lansari")
    plt.ylabel("Probabilitate")
    plt.legend()

    # Afișarea graficului
    plt.show()
grafic()
