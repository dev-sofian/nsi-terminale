### 📚 Explication 1 — Variables, types et le piège du `=` / `==`

**🎯 Objectif de ce bloc** : identifier une erreur de syntaxe ou de logique liée aux variables, types et conditions.

**🟢 Guidé**
```python
age = 17          # affectation : on range 17 dans la boîte "age"
if age == 17:      # test d'égalité : on compare age à 17
    print("Tu as 17 ans")
```
Vérification : que se passe-t-il si on écrit `if age = 17:` au lieu de `if age == 17:` ? (essaie, Python va te renvoyer une erreur — lis le message.)

 - Si on écrit `if age = 17:` au lieu de `if age == 17:`, Python renverra une erreur de syntaxe : l'interpréteur attend une comparaison (`==`) mais trouve une affectation (`=`).

**🟡 Intermédiaire** — `=` affecte une valeur, `==` compare deux valeurs. Une erreur de typage classique : `"17" == 17` renvoie `False` (chaîne vs entier).
**Point de vigilance** : `input()` renvoie toujours une chaîne de caractères, même si l'utilisateur tape un nombre — il faut la convertir avec `int()` ou `float()`.

**🔴 Expert** — Question ouverte : pourquoi `0.1 + 0.2 == 0.3` renvoie-t-il `False` en Python ? Teste-le.

 - En Python (et dans la plupart des langages), les nombres à virgule flottante (`float`) sont représentés en base binaire avec une précision limitée. Certaines décimales (comme `0.1`) n'ont pas de représentation binaire exacte, ce qui provoque de petites erreurs d'arrondi. Exemple :

```python
>>> 0.1 + 0.2
0.30000000000000004
>>> 0.1 + 0.2 == 0.3
False
```

### 📚 Explication 2 — Boucles `for` et `while`

**🎯 Objectif de ce bloc** : écrire une boucle bornée (`for`) et une boucle non bornée (`while`) adaptées à un énoncé.

**🟢 Guidé**
```python
for i in range(1, 6):
    print(i)          # affiche 1 2 3 4 5

compteur = 0
while compteur < 3:
    print(compteur)
    compteur = compteur + 1   # sans cette ligne, boucle infinie !
```
Vérification : que se passe-t-il si on supprime la ligne `compteur = compteur + 1` ?

 - Si on supprime la ligne `compteur = compteur + 1`, la boucle `while` n'atteindra jamais la condition nécessaire à sa fermeture et continura de se répéter en affichant indéfiniment le `compteur = 0` dans la console. La condition doit obligatoirement être atteinte à l'intérieur de la boucle.

**🟡 Intermédiaire** — `for` quand on connaît à l'avance le nombre de répétitions, `while` quand on répète "tant qu'une condition est vraie" (nombre de tours inconnu).
**Point de vigilance** : une boucle `while` doit toujours faire évoluer la variable testée dans sa condition.

**🔴 Expert** — Question ouverte : peux-tu réécrire une boucle `for i in range(5)` en `while` strictement équivalente ?

```python
i = 0
while i < 5:
    i += 1
```

### 📚 Explication 3 — Tracer l'exécution d'un programme

**🎯 Objectif de ce bloc** : prédire la sortie d'un programme court avant de l'exécuter.

**🟢 Guidé**
```python
total = 0
for x in [3, 5, 2]:
    total = total + x
print(total)
```
Vérification : sans exécuter, que vaut `total` à la fin ? Vérifie ensuite en exécutant.

 - `total` devrait valoir `10` à la fin du programme.

**🟡 Intermédiaire** — Tracer un programme, c'est noter la valeur de chaque variable après chaque ligne exécutée, comme un tableau.
**Point de vigilance** : bien distinguer la valeur *avant* et *après* chaque instruction.

**🔴 Expert** — Question ouverte : dans une boucle `while`, comment prouverais-tu qu'elle se termine forcément (variant de boucle) ?

 - Dans une boucle `while`, pour prouver qu'elle se termine forcément, il faut vérifier qu'à l'intérieur de la boucle, on se rapproche de plus en plus de la condition de la boucle. Lorsque cette condition est atteinte, la boucle se termine.