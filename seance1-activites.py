age = int(input("Quel âge as-tu ? "))
if age >= 18:      # complète avec le bon symbole de comparaison
    print("majeur")
else:
    print("mineur")

# ---

note = float(input("Quelle est ta note sur 20 ? "))
if note >= 16:
    print("très bien")
elif note >= 14:
    print("bien")
elif note >= 12:
    print("assez bien")
# il manque un cas !
else:
    print("passable")

# ---

a = 0.1 + 0.2
print(a == 0.3)        # affiche False !
print(abs(a - 0.3) < 1e-9)   # affiche True
"""
- La seconde ligne compare la différence absolue à une petite tolérance pour tenir compte des erreurs d'arrondi liées à l'imprécision des flottants, évitant ainsi les faux négatifs.
"""

# ---

for i in range(1, 6):   # complète pour afficher 1 à 5
    print(i)

# ---

n = int(input("Compte à rebours depuis : "))
while n > 0:      # complète la condition
    print(n)
    n = n - 1
print("Décollage !")

# ---

def for_en_while(n):
    # réécris range(n) avec une boucle while, doit afficher les mêmes valeurs
    i = 0
    while i < n:
        print(i)
        i += 1
    pass

def for_classique(n):
    for i in range(n):
        print(i)