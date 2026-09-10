def addition(n1, n2):
    return print(n1 + n2)

def soustraction(n1, n2):
    return print(n1 - n2)

def multiplication(n1, n2):
    return print(n1 * n2)

def division(n1, n2):
    if n2 == 0:
        return None
    return print(n1 / n2)

def puissance(n1, n2):
    return print(n1**n2)

def calculatrice(n1, n2):
    entree = (input("Que souhaitez vous faire ? (Add, Sub, Mult, Div, Pow, Exit) : "))
    if entree == "Add":
        addition(n1, n2)
    elif entree == "Sub":
        soustraction(n1, n2)
    elif entree == "Mult":
        multiplication(n1, n2)
    elif entree == "Div":
        division(n1, n2)
    elif entree == "Pow":
        puissance(n1, n2)
    elif entree == "Exit":
        return
    no1 = int(input("Entrez nouveau nombre n°1 : "))
    no2 = int(input("Entrez nouveau nombre n°2 : "))
    calculatrice(no1, no2)

calculatrice(100, 20)