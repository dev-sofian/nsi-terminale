eleves = [("Léa", 15), ("Tom", 8), ("Zoé", 12)]
resume = [f"{nom} : {'admis' if note >= 10 else 'ajourné'}" for nom, note in eleves]
print(resume)
def admission(n):
    for i, eleve in enumerate(eleves):
        if i == n:
            n += 1
            if eleve[1] >= 10:
                yield f"{eleve[0]} : admis"
            else:
                yield f"{eleve[0]} : ajourné"

for valeur in admission(0):
    print(valeur)