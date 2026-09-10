### 📚 Explication 1 — Décomposer un problème en pseudo-code

**🎯 Objectif de ce bloc** : décomposer un énoncé en étapes numérotées, indépendamment de la syntaxe.

**Problème :** trouver le plus grand nombre d'une liste


**🟢 Guidé**
```
Problème : trouver le plus grand nombre d'une liste
1. Je garde en mémoire le premier nombre comme "le plus grand pour l'instant"
2. Je regarde chaque nombre suivant un par un
3. Si ce nombre est plus grand, je le remplace
4. À la fin, "le plus grand pour l'instant" est la réponse
```
Vérification : sur la liste `[3, 9, 2]`, déroule les 4 étapes à la main.

```
1. je garde en mémoire le nombre 3.
2. je check si 9 > 3. vrai
3. je remplace la valeur 3 par 9 dans la mémoire.
4. je check si 2 > 9. faux
5. le plus grand de la liste est 9.
```

**🟡 Intermédiaire** — Le pseudo-code vérifie la logique avant de se soucier de la syntaxe Python.
**Point de vigilance** : un pseudo-code qui "oublie" un cas (liste vide) donnera un programme qui plante.

**🔴 Expert** — Question ouverte : écris deux pseudo-codes différents pour le même problème (un qui trie d'abord, un qui ne trie pas) — lequel te semble le plus économe ?

```

```

### 📚 Explication 2 — Traduire le pseudo-code en Python

**🎯 Objectif de ce bloc** : traduire fidèlement un pseudo-code en programme Python fonctionnel.

**🟢 Guidé**
```python
liste = [3, 9, 2]
plus_grand = liste[0]        # étape 1
for nombre in liste[1:]:     # étape 2
    if nombre > plus_grand:  # étape 3
        plus_grand = nombre
print(plus_grand)            # étape 4
```
Vérification : pourquoi commence-t-on la boucle à `liste[1:]` et pas à `liste[0]` ?

- Parce que le premier élément de la liste (liste[0]) est déjà considéré comme le maximum. Donc on n'a pas besoin de comparer le premier élement avec lui même. ça nous optimise d'une étape.

**🟡 Intermédiaire** — Chaque étape du pseudo-code doit correspondre à une ou plusieurs lignes Python, dans le même ordre.
**Point de vigilance** : toujours dérouler mentalement un cas limite (liste vide, un seul élément) avant de coder.

**🔴 Expert** — Question ouverte : peux-tu écrire une version qui trouve le plus grand nombre EN TRIANT D'ABORD la liste (`sorted(liste)[-1]`) ? Compare avec la version qui parcourt une seule fois.

```python
sorted(liste)[-1]
```