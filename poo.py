class Voiture:
    def __init__(self, marque, annee, prix, places, kilometres, capacite, remplissage):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        self.places = places
        self.kilometres = kilometres or 0
        self.capacite = capacite or 1
        self.remplissage = remplissage or 0
        if self.remplissage > self.capacite:
            self.remplissage = self.capacite


    def conduire(self, passagers, destination):
        distance = 0
        if self.places < passagers:
            return "Trop de passagers !"
        while self.remplissage > 0 or distance < destination:
            self.remplissage -= 1
            self.kilometres += 1
            distance += 1
        if distance >= destination:
            return "Arrivé à destination !"
        else:
            return "Panne de carburant !"

v1 = Voiture("Peugeot", 2019, 25900, 5, 3000, 650, 500)
print(v1.conduire(4, 5000))