from math import sqrt

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

def racine_carree(n1):
    return print(sqrt(n1))

def calculatrice():
    """
    Fonction simulant une calculatrice. Les opérations possibles sont les suivantes : 
    a+b, a-b, a*b, a/b (b non nul), a**b, sqrt(a)
    @return : Lorsque entree == "Exit".
    """
    n1, n2 = 0, 0
    entree = (input("Que souhaitez vous faire ? (Add, Sub, Mult, Div, Pow, Sqrt, Exit) : "))
    if entree == "Sqrt":
        n1 = int(input("Entrez nouveau nombre n°1 : "))
        racine_carree(n1)
    elif entree == "Exit":
        return
    else:
        n1 = int(input("Entrez nouveau nombre n°1 : "))
        n2 = int(input("Entrez nouveau nombre n°2 : "))
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

    calculatrice()

calculatrice()