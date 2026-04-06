import csv

def creer_liste():
    with open("dico.csv", encoding="utf8", newline="") as monFichier:
        monContenu = csv.reader(monFichier, delimiter = ",")
        # on crée une liste des clients
        ma_liste = []
        for row in monContenu:
            # On remplit la liste des mots
            ma_liste.append(row[0])
    return ma_liste

mesMots=creer_liste()

for i in range(1000):
    print(mesMots[i])