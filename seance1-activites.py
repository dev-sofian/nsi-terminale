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

# ---

x = 2
y = 5
x = y
y = x
print(x==5, y==5)
"""
Certaines personnes se trompent en prédisant les valeurs de x et y au moment du print() parce qu'ils pensent que leurs valeurs initiales ont été interchangées, or, on voit que x prend la valeur de y AVANT que y prenne la valeur de x.
Pour corriger l'erreur, on peut introduire une troisième variable à laquelle on affecte l'ancienne valeur de x ou de y pour permettre le changement de valeurs.
On peut également écrire dans la même ligne : x, y = y, x.
"""

# ---

def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

print(factorielle(4))
# factorielle 4 : 4*factorielle(3)*factorielle(2)*factorielle(1)*factorielle(0) = 4*3*2*1*1 = 24

"""
Tant que n >= 0, la fonction se finit forcément. La fonction s'auto-appelle jusqu'à une limite définie à l'intérieur de la fonction elle-même; si l'argument 'n' est égal à 0, la fonction retourne 1 et se ferme. Ainsi, cela règle à la fois le problème de la fonction qui s'appelle à l'infini, et le fait que la factorielle ne met pas en facteur le nombre 0 (renvoie 1 à la place, qui ne change rien).
"""

# ---
