"""#### ✏️ Activité 1

**🟢 Guidé** — Remets ces 4 lignes de pseudo-code dans le bon ordre pour "compter les nombres pairs d'une liste" :
```

b) Je pars d'un compteur à 0
a) Je regarde chaque nombre de la liste
d) Si le nombre est pair, j'ajoute 1 au compteur
c) À la fin, le compteur est la réponse

```

**🟡 Intermédiaire** — Écris le pseudo-code puis le code Python de `rechercher_nom(carnet, nom)`.
*Indice : que se passe-t-il si `carnet` est vide ?*

**🔴 Expert** — Sans pseudo-code fourni : conçois un algorithme qui trouve le minimum ET le maximum d'une liste en un seul parcours.

---
"""

from random import randint

def minimaxi(liste):
    mini = liste[0]
    maxi = liste[0]
    for i in liste:
        if mini > i:
            mini = i
        if maxi < i:
            maxi = i
    print(liste, mini, maxi)

minimaxi([randint(-100, 100) for i in range(15)])

liste = [4, 7, 1, 9]
total = 0
for x in liste:
    total = total + x
print(total)

def rechercher_nom(carnet, nom):
    for x in carnet:
        if x == nom:
            return True
    return False
    # traduis ton pseudo-code de l'activité 1 ici

carnet = ["Léa", "Tom"]
print(rechercher_nom(carnet, "Tom"))   # attendu : True
print(rechercher_nom([], "Léa"))       # attendu : False

assert rechercher_nom(carnet, "Tom") == False, "c'est faux 😂"