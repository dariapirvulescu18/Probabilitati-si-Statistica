import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# def simulare1(num_pas,num_simulari):
#     np.random.seed(42)  # pentru reproducibilitate
#     trajectories = np.zeros((num_simulari, num_pas + 1))
#
#     for i in range(num_simulari):
#         steps = np.random.choice([-1, 1], size=num_pas)
#         trajectory = np.cumsum(steps)
#         trajectories[i, 1:] = trajectory
#
#     # Plotare traiectorii
#     plt.figure(figsize=(10, 6))
#     plt.title('Evoluția poziției betivului după 10 pasi')
#     plt.xlabel('Numar de pasi')
#     plt.ylabel('Poziție')
#
#     for i in range(num_simulari):
#         plt.plot(range(num_pas + 1), trajectories[i, :])
#
#     plt.show()
#
#
#     np.random.seed(42)  # pentru reproducibilitate
#
#     # Simulare
#     num_pas = 10
#     num_simulari = 10000
#
#     # Inițializare array-uri pentru stocarea traiectoriilor
#     trajectories = np.zeros((num_simulari, num_pas + 1))
#
#     for i in range(num_simulari):
#         # Generare pasi la stânga (valoare -1) sau dreapta (valoare 1) cu probabilități egale
#         steps = np.random.choice([-1, 1], size=num_pas)
#         trajectory = np.cumsum(steps)
#         trajectories[i, 1:] = trajectory
#
#     # Plotare traiectorii
#     plt.figure(figsize=(10, 6))
#     plt.title('Evoluția poziției betivului după 10 pași')
#     plt.xlabel('Număr de pași')
#     plt.ylabel('Poziție')
#
#     for i in range(num_simulari):
#         plt.plot(range(num_pas + 1), trajectories[i, :],alpha=0.05)
#
#     plt.show()
#
#
# simulare1(10,10000)

# def simulare2(num_pas,num_simulari):
#     np.random.seed(42)
#
#     # Inițializare array pentru stocarea pozițiilor finale
#     pozitii_finale = np.zeros(num_simulari)
#
#     for i in range(num_simulari):
#         # Generare pasi la stânga (valoare -1) sau dreapta (valoare 1) cu probabilități egale
#         steps = np.random.choice([-1, 1], size=num_pas)
#         trajectory = np.cumsum(steps)
#         pozitii_finale[i] = trajectory[-1]
#
#     # Construirea histogramă
#     plt.figure(figsize=(10, 10))
#     plt.hist(pozitii_finale, bins=[np.unique(pozitii_finale)-1].append(np.max(pozitii_finale)+1), density=True, alpha=0.7, color='pink', edgecolor='black')
#
#     # Aproximarea cu o distribuție normală
#     x = np.linspace(-10, 10, 100)
#
#     y = 1 / np.sqrt(2 * np.pi * 10) * np.exp(-x ** 2 / (2 * 10))
#     plt.plot(x,y,'r-')
#     # Adăugare etichete
#     plt.title('Histograma și aproximația cu o distribuție normală')
#     plt.xlabel('Poziție finală')
#     plt.ylabel('Densitate de probabilitate')
#
#     # Adăugare legenda
#     plt.legend(['Distribuție normală fit', 'Histogramă'])
#
#     plt.show()
#
# simulare2(10,10000)

# def simulare3(num_luni,num_simulations):
#
#
#     np.random.seed(42)  # Asigurăm reproducibilitatea simulării
#
#
#     crestere_percent = 0.5
#     scadere_percent = -0.4
#
#     # Inițializăm matricea pentru a stoca traiectoriile
#     traiectorii = np.zeros((num_simulations, num_luni))
#
#     # Simulăm evoluția actiunii
#     for i in range(num_simulations):
#         valoare = 1.0  # Valoarea inițială a acțiunii
#         for j in range(num_luni):
#             # Generăm un număr aleatoriu între 0 și 1
#             probabilitate = np.random.rand()
#
#             # Actualizăm valoarea în funcție de probabilitate
#             if probabilitate < 0.5:
#                 valoare *= 1 + crestere_percent
#             else:
#                 valoare *= 1 + scadere_percent
#
#             # Salvăm valoarea în matrice
#             traiectorii[i, j] = valoare
#
#     # Plotăm traiectoriile
#     plt.figure(figsize=(10, 6))
#     plt.plot(np.arange(1, num_luni + 1), traiectorii.T, color='blue', alpha=0.1)
#     plt.title('Evoluția valorii acțiunii în timp (10000 de simulări)')
#     plt.xlabel('Luni')
#     plt.ylabel('Valoare acțiune')
#     plt.show()
#
#
# simulare3(12,10000)

# def simulare4():
#     np.random.seed(42)  # Asigurăm reproducibilitatea simulării
#
#     # Parametrii
#     num_simulations = 10000
#     num_luni = 12
#     crestere_percent = 0.5
#     scadere_percent = -0.4
#
#     # Inițializăm matricea pentru a stoca valorile finale
#     valori_finale = np.zeros(num_simulations)
#
#     # Simulăm evoluția actiunii
#     for i in range(num_simulations):
#         valoare = 1.0  # Valoarea inițială a acțiunii
#         for j in range(num_luni):
#             # Generăm un număr aleatoriu între 0 și 1
#             probabilitate = np.random.rand()
#
#             # Actualizăm valoarea în funcție de probabilitate
#             if probabilitate < 0.5:
#                 valoare *= 1 + crestere_percent
#             else:
#                 valoare *= 1 + scadere_percent
#
#         # Salvăm valoarea finală în vector
#         valori_finale[i] = valoare
#
#     # Construim histograma
#     plt.figure(figsize=(10, 6))
#     plt.hist(valori_finale, bins=50, color='blue', alpha=0.7, edgecolor='black')
#
#     # Adăugăm linii pentru media și mediana valorilor finale
#     media = np.mean(valori_finale)
#     mediana = np.median(valori_finale)
#
#     plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Media = {media:.2f}')
#     plt.axvline(mediana, color='green', linestyle='dashed', linewidth=2, label=f'Mediana = {mediana:.2f}')
#
#     plt.title('Histograma Valorilor Finale ale Acțiunii (10000 de simulări)')
#     plt.xlabel('Valoare Acțiune Finală')
#     plt.ylabel('Frecvență')
#     plt.legend()
#     plt.show()
#
# simulare4()

def simulare3(num_luni,num_simulations):
    np.random.seed(42)  # Asigurăm reproducibilitatea simulării


    crestere_percent = 0.5
    scadere_percent = -0.4

    # Inițializăm matricea pentru a stoca traiectoriile
    traiectorii = np.zeros((num_simulations, num_luni))

    # Simulăm evoluția actiunii
    for i in range(num_simulations):
        valoare = 1.0  # Valoarea inițială a acțiunii
        for j in range(num_luni):
            # Generăm un număr aleatoriu între 0 și 1
            probabilitate = np.random.rand()

            # Actualizăm valoarea în funcție de probabilitate
            if probabilitate < 0.5:
                valoare *= 1 + crestere_percent
            else:
                valoare *= 1 + scadere_percent

            # Salvăm valoarea în matrice
            traiectorii[i, j] = valoare

    # Plotăm traiectoriile
    plt.figure(figsize=(10, 6))
    plt.semilogy(np.arange(1, num_luni + 1), traiectorii.T, color='blue', alpha=0.1)
    plt.title('Evoluția valorii acțiunii în timp (10000 de simulări)')
    plt.xlabel('Luni')
    plt.ylabel('Valoare acțiune')
    plt.show()


simulare3(12,10000)
def simulare4():
    np.random.seed(42)  # Asigurăm reproducibilitatea simulării

    # Parametrii
    num_simulations = 10000
    num_luni = 12
    crestere_percent = 0.5
    scadere_percent = -0.4

    # Inițializăm matricea pentru a stoca valorile finale
    valori_finale = np.zeros(num_simulations)

    # Simulăm evoluția actiunii
    for i in range(num_simulations):
        valoare = 1.0  # Valoarea inițială a acțiunii
        for j in range(num_luni):
            # Generăm un număr aleatoriu între 0 și 1
            probabilitate = np.random.rand()

            # Actualizăm valoarea în funcție de probabilitate
            if probabilitate < 0.5:
                valoare *= 1 + crestere_percent
            else:
                valoare *= 1 + scadere_percent

        # Salvăm valoarea finală în vector
        valori_finale[i] = valoare

    # Construim histograma
    plt.figure(figsize=(10, 6))
    plt.hist(np.log(valori_finale), bins=30, color='blue', alpha=0.7, edgecolor='black', log=True)

    # Adăugăm linii pentru media și mediana valorilor finale
    media = np.mean(np.log(valori_finale))
    mediana = np.median(np.log(valori_finale))

    plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Media = {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='dashed', linewidth=2, label=f'Mediana = {mediana:.2f}')

    plt.title('Histograma Valorilor Finale ale Acțiunii (10000 de simulări)')
    plt.xlabel('Valoare Acțiune Finală')
    plt.ylabel('Frecvență')
    plt.legend()
    plt.show()

simulare4()
