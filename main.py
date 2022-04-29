import os
import shutil


def backup():
    print("Ciao")
    print()
    percorso = input("Percorso: ")
    estensione = input("Estensione: ")
    cartella = input("Cartella: ")
    if not os.path.isdir(cartella):
        os.makedirs(cartella)
    if os.path.isdir(percorso):
        for c, _, f in os.walk(percorso):
            for file in f:
                if file.endswith(estensione):
                    match = os.path.join(c, file)
                    shutil.copy(match, cartella)
    else:
        print("Errore path")

backup()
