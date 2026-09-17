from random import randint

def tri_croissant(liste):
    for i in range(len(liste)):
        for j in range(len(liste)):
            if liste[j] > liste[i]:
                liste[j], liste[i] = liste[i], liste[j]
    return


def dichotomie(liste, valeur):
    tri_croissant(liste)
    gauche, droite = 0, len(liste) - 1
    while gauche <= droite:
        milieu = gauche + droite // 2
        if liste[milieu] == valeur:
            print(f"Milieu : {milieu} : {liste[milieu]} est égal à Valeur : {valeur}")
            return True
        elif liste[milieu] < valeur:
            print(f"Milieu : {milieu} : {liste[milieu]} est inférieur à Valeur : {valeur}")
            gauche = milieu + 1
        else:
            print(f"Milieu : {milieu} : {liste[milieu]} est supérieur à Valeur : {valeur}")
            droite = milieu - 1
    return False

lst = [randint(0, 20) for i in range(9)]

valeur = lst[5]

assert dichotomie(lst, valeur) == True

def renverse_chaine(chaine):
    chaine_inverse=""
    for lettre in chaine:
        chaine_inverse = lettre + chaine_inverse
    return chaine_inverse

assert renverse_chaine("banana")=="ananab"