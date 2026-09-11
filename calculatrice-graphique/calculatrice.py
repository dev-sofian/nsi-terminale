from math import sqrt
import pyxel

class Calculatrice:
    def __init__(self):
        self.resultat = 0
        self.operateur = ""
        self.n1 = 0
        self.n2 = 0
    def addition(self):
        self.resultat = self.n1 + self.n2
    def soustraction(self):
        self.resultat = self.n1 - self.n2
    def multiplication(self):
        self.resultat = self.n1 * self.n2
    def division(self):
        if self.n2 == 0:
            return None
        self.resultat = self.n1 / self.n2
    def puissance(self):
        self.resultat = self.n1 ** self.n2
    def racine_carree(self):
        self.resultat = sqrt(self.n1)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, f"n1: {self.n1}", 7)
        pyxel.text(10, 20, f"n2: {self.n2}", 7)
        pyxel.text(10, 30, f"Opérateur: {self.operateur}", 7)
        pyxel.text(10, 40, f"Résultat: {self.resultat}", 7)