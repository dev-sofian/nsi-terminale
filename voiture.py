from datetime import date
from math import cos, sin, radians
from random import sample, randint, choice

class Voiture:

    CAPACITE_MAX = 50
    CONSOMMATION = 0.07

    def __init__(self, marque, couleur, proprietaire, immatriculation, type, pos_x=0, pos_y=0, direction=0, kilometrage=0, reservoir=40.0):
        self.marque = marque
        self.couleur = couleur
        self.proprietaire = proprietaire
        self.immatriculation = immatriculation
        self.type = type
        self.x = pos_x
        self.y = pos_y
        self.direction = direction
        self.kilometrage = kilometrage
        self.reservoir = reservoir
        self.historique = []

    def __str__(self):
        return f"Marque : {self.marque} -- Couleur : {self.couleur} -- Immatriculation : {self.immatriculation} -- Propriétaire : {self.proprietaire} -- Coordonnées : {(self.x, self.y)} -- Kilométrage : {self.kilometrage} -- Historique : {self.historique}"

    def rouler(self, km, mode):
        if self.CONSOMMATION * km > self.reservoir:
            return
        self.reservoir -= self.CONSOMMATION * km
        self.kilometrage += km
        if mode == "avancer":
            self.x += cos(radians(self.direction)) * km
            self.y += sin(radians(self.direction)) * km
        else:
            self.x -= cos(radians(self.direction)) * km
            self.y -= sin(radians(self.direction)) * km
        
        self.historique.append((km, date.today()))
        print(f"la voiture de {self.proprietaire} a roulé {km} km. Il lui reste {self.reservoir} L de carburant.")

    def tourner(self, dir):
        if isinstance(dir, int):
            self.direction += dir
        elif dir == "droite":
            self.direction -= 90
        else:
            self.direction += 90

    def faire_le_plein(self, montant):
        if self.reservoir + montant > self.CAPACITE_MAX:
            self.reservoir = self.CAPACITE_MAX
        else:
            self.reservoir += montant

liste_noms = ["Lucas", "Emma", "Thomas", "Léa", "Hugo", "Marin", "Nathan", "José", 
    "Enzo", "Sarah", "Louise", "Jade", "Arthur", "Joséphine", "Gabriel", "Camille", "Sofian", "Alain", "Vianney"]
liste_couleurs = ["Rouge", "Bleu", "Noir", "Blanc", "Gris", "Vert", "Jaune"]
liste_marques = ["Peugeot", "Renault", "Citroën", "Tesla", "Toyota", "BMW", "Audi", "Mercedes"]
liste_moteurs = ["essence", "diesel", "electrique", "hybride"]
    
garage = []

nb = 8

for i in range(nb):
    nom = choice(liste_noms)
    nouvelle_voiture = Voiture(
        marque=choice(liste_marques),
        couleur=choice(liste_couleurs),
        proprietaire=nom,
        immatriculation=nom+"FR"+str(randint(100, 999)),
        type=choice(liste_moteurs),
        pos_x=randint(-100, 100),
        pos_y=randint(-100, 100),
        direction=randint(0, 360),
        reservoir=randint(30, 50)
    )
    garage.append(nouvelle_voiture)

for i in range(randint(10, 35)):
    garage[randint(0, nb-1)].tourner(randint(0, 360))
    garage[randint(0, nb-1)].rouler(randint(100, 1000), "avancer")
    garage[randint(0, nb-1)].faire_le_plein(randint(20, 30))



for voiture in garage:
    print(str(voiture))