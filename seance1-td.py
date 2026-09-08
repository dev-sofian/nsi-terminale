for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# ---

total = 0
note = 0
somme = 0

while note != -1:
    note = int(input("Veuillez saisir une note. : "))
    total += note
    somme += 1
somme = total/somme
print(f"Vous avez une moyenne de {somme}/20.")