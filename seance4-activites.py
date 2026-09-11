from random import randint

def plancher_et_plafond(notes: list, mini: int, maxi: int) -> list:
    """
    Fonction ajoutant un plancher et un plafond à une liste, insérant toute valeur hors des limites dans l'intervalle.
    @params : notes: une liste de nombres entiers; mini: le plancher de l'intervalle; maxi: le plafond de l'intervalle
    @return : renvoie la liste modifiée.
    """
    for i in range(len(notes)):
        if notes[i] < mini:
            notes[i] = mini
        elif notes[i] > maxi:
            notes[i] = maxi
    return notes

print(plancher_et_plafond([randint(-100, 100) for i in range(15)], 0, 20))

carnet = [("Léa", "0611223344"), ("Tom", "0622334455"), ("Zoé", "0633445566")]

noms = [carnet[i][0] for i in range(len(carnet))]
print(noms)

contacts = [carnet[i] for i in range(len(carnet)) if carnet[i][1].startswith("06")]
print(contacts)

liste_paires = [i for i in range(2, 13, 2)]
print(liste_paires)

notes = [14, 8, 19, 5, 12, 17]

def verifListe(liste: list) -> tuple:
    mini = liste[0]
    maxi = liste[0]
    moyenne = 0
    for i in range(len(liste)):
        if mini > liste[i]:
            mini = liste[i]
        if maxi < liste[i]:
            maxi = liste[i]
        moyenne += liste[i]
    return (mini, maxi, moyenne/len(liste))

print(verifListe(notes))