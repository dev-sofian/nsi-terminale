import csv

def importer_table(chemin_fichier):
    """
        Précondition  : chemin_fichier pointe vers un CSV avec un en-tête
        Postcondition : renvoie une liste de dictionnaires, une par ligne du CSV
    """
    table = []
    try:
        with open(chemin_fichier, newline="", encoding="utf-8") as fichier:
            lecteur = csv.DictReader(fichier)
            for ligne in lecteur:
                table.append(ligne)
    except IOError:
        return f"FILE {chemin_fichier} NOT FOUND."
    return table

print(importer_table("eleves.csv"))
print(importer_table("jean.csv"))

def rechercher(table, classe, note_min):
    liste = []
    for ligne in table:
        if ligne["classe"] == classe and int(ligne["note"]) >= note_min:
            liste.append(ligne)
    return liste

table = [
    {"nom": "Léa", "classe": "TG1", "note": 15},
    {"nom": "Tom", "classe": "TG2", "note": 8},
    {"nom": "Zoé", "classe": "TG1", "note": 12},
    {"nom": "Nino", "classe": "TG2", "note": 17}
]

print(rechercher(table, "TG2", 10))

def rechercher_critere(table, condition):
    """
    condition est une fonction qui prend une ligne (dictionnaire) et renvoie True/False
    """

    return [ligne for ligne in table if condition(ligne)]

resultat = rechercher_critere(table, lambda ligne: ligne["note"] >= 10 and ligne["classe"] == "TG1" and ligne["nom"].startswith("Z"))
print(resultat)