for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# ---

total = 0
note = 0
somme = 0
"""
while note != -1:
    note = int(input("Veuillez saisir une note. : "))
    if note != -1:
        total += note
        somme += 1
        
somme = total/somme
print(f"Vous avez une moyenne de {somme}/20.")
"""
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

#plus_ou_moins(randint(0, 100))

# ---

import time

def for_en_while(indice, but):
    if indice == None:
        indice = 0
    else:
        but = but+1
    while indice < but:
        print(indice)
        indice += 1

def while_en_for(condition):
    for _ in range(1 if condition else 10000):
        print("Boucle")

for_en_while(None, 50)
booleen = False
while_en_for(booleen)
time.sleep(.15)
booleen = True



def moyenne_ponderee():
    note = 0
    coeff = 0
    total = 0
    i = 0
    while note != -1:
        i += coeff
        total += note*coeff
        print(total/i)
        note = int(input("Entrez votre note : "))
        coeff = int(input("Entrez votre coeff : "))
            
    print(total/i)

#moyenne_ponderee()

def compteur(n, pas):
    for i in range(n, 0, pas):
        print(i)
    print("boom")

compteur(10, -1)