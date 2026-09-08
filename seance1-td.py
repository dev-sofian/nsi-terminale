for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# ---

total = 0
note = 0
somme = 0

while note != -1:
    note = int(input("Veuillez saisir une note. : "))
    if note != -1:
        total += note
        somme += 1
        
somme = total/somme
print(f"Vous avez une moyenne de {somme}/20.")

# ---

from random import randint

def plus_ou_moins(n):
    tentatives = 0
    choisi = -1
    while choisi != n:
        choisi = int(input("Choisissez un nombre entre 0 et 100. : "))
        if choisi < n:
            print("Plus grand !")
        elif choisi > n:
            print("Moins grand !")
        tentatives += 1
    print(f"Vous avez trouvé le bon nombre {n} en {tentatives} tentatives.")

plus_ou_moins(randint(0, 100))