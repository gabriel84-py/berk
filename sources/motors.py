from random import randint

def tri_selection(tab):
    for i in range(len(tab)-1):
        mini = tab[i]
        i_mini = i
        for j in range(i,len(tab)):
            if tab[j] < mini:
                mini = tab[j]
                i_mini = j
        tab.pop(i_mini)
        tab.insert(i,mini)
    return tab

def alea(a,b):
    return [randint(0,b) for i in range(a)]

#print(tri_selection(alea(10,10)))


def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre etait ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre etait ", nb_mystere)

plus_ou_moins()
