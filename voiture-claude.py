"""
Simulation de garage avec visualisation Pygame.

Reprend fidèlement la logique de la classe Voiture d'origine (rouler,
tourner, faire_le_plein) et ajoute une fenêtre graphique qui montre les
voitures se déplacer en temps réel sur un plan 2D.

Installation :
    pip install pygame

Lancement :
    python simulation_voitures_pygame.py
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from math import cos, sin, radians
from random import choice, randint

import pygame

# --------------------------------------------------------------------------- #
# Modèle : la classe Voiture (logique inchangée par rapport à l'original)
# --------------------------------------------------------------------------- #


class Voiture:

    CAPACITE_MAX = 50
    CONSOMMATION = 0.07

    def __init__(self, marque, couleur, proprietaire, immatriculation, type,
                 pos_x=0, pos_y=0, direction=0, kilometrage=0, reservoir=40.0):
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

        # Position affichée séparément de la position réelle : elle "glisse"
        # progressivement vers (x, y) à chaque frame, ce qui donne une
        # animation fluide même si rouler() déplace la voiture d'un coup.
        self.x_affiche = float(pos_x)
        self.y_affiche = float(pos_y)

    def __str__(self):
        return (f"Marque : {self.marque} -- Couleur : {self.couleur} -- "
                f"Immatriculation : {self.immatriculation} -- "
                f"Propriétaire : {self.proprietaire} -- "
                f"Coordonnées : {(self.x, self.y)} -- "
                f"Kilométrage : {self.kilometrage} -- Historique : {self.historique}")

    def rouler(self, km, mode):
        if self.CONSOMMATION * km > self.reservoir:
            return
        self.reservoir -= self.CONSOMMATION * km
        self.kilometrage += km
        signe = 1 if mode == "avancer" else -1
        self.x += signe * cos(radians(self.direction)) * km
        self.y += signe * sin(radians(self.direction)) * km
        self.historique.append((km, date.today()))

    def tourner(self, dir):
        if isinstance(dir, int):
            self.direction += dir
        elif dir == "droite":
            self.direction -= 90
        else:
            self.direction += 90

    def faire_le_plein(self, montant):
        self.reservoir = min(self.reservoir + montant, self.CAPACITE_MAX)

    def maj_affichage(self, vitesse_lissage=0.08):
        """Fait avancer doucement la position affichée vers la position réelle."""
        self.x_affiche += (self.x - self.x_affiche) * vitesse_lissage
        self.y_affiche += (self.y - self.y_affiche) * vitesse_lissage


# --------------------------------------------------------------------------- #
# Génération du garage
# --------------------------------------------------------------------------- #

LISTE_NOMS = ["Lucas", "Emma", "Thomas", "Léa", "Hugo", "Marin", "Nathan", "José",
              "Enzo", "Sarah", "Louise", "Jade", "Arthur", "Joséphine", "Gabriel",
              "Camille", "Sofian", "Alain", "Vianney"]
LISTE_COULEURS_RGB = {
    "Rouge": (220, 60, 60), "Bleu": (60, 100, 220), "Noir": (40, 40, 40),
    "Blanc": (235, 235, 235), "Gris": (140, 140, 140), "Vert": (60, 180, 90),
    "Jaune": (230, 200, 50),
}
LISTE_MARQUES = ["Peugeot", "Renault", "Citroën", "Tesla", "Toyota", "BMW", "Audi", "Mercedes"]
LISTE_MOTEURS = ["essence", "diesel", "electrique", "hybride"]


def creer_garage(nb=8):
    garage = []
    for _ in range(nb):
        nom = choice(LISTE_NOMS)
        garage.append(Voiture(
            marque=choice(LISTE_MARQUES),
            couleur=choice(list(LISTE_COULEURS_RGB)),
            proprietaire=nom,
            immatriculation=f"{nom}FR{randint(100, 999)}",
            type=choice(LISTE_MOTEURS),
            pos_x=randint(-100, 100),
            pos_y=randint(-100, 100),
            direction=randint(0, 360),
            reservoir=randint(30, 50),
        ))
    return garage


def etape_aleatoire(garage):
    """Une "étape" de simulation : équivalent d'un tour de la boucle d'origine."""
    choice(garage).tourner(randint(0, 360))
    choice(garage).rouler(randint(100, 1000), "avancer")
    choice(garage).faire_le_plein(randint(20, 30))


# --------------------------------------------------------------------------- #
# Affichage Pygame
# --------------------------------------------------------------------------- #

LARGEUR, HAUTEUR = 1000, 700
MARGE_CAMERA = 80
INTERVALLE_ETAPE_MS = 600  # une étape de simulation toutes les 600 ms


def calculer_transformation(garage):
    """Calcule l'échelle et le décalage pour que toutes les voitures tiennent à l'écran."""
    xs = [v.x_affiche for v in garage]
    ys = [v.y_affiche for v in garage]
    x_min, x_max = min(xs) - 20, max(xs) + 20
    y_min, y_max = min(ys) - 20, max(ys) + 20

    largeur_monde = max(x_max - x_min, 1)
    hauteur_monde = max(y_max - y_min, 1)

    echelle = min(
        (LARGEUR - 2 * MARGE_CAMERA) / largeur_monde,
        (HAUTEUR - 2 * MARGE_CAMERA) / hauteur_monde,
    )
    centre_x_monde = (x_min + x_max) / 2
    centre_y_monde = (y_min + y_max) / 2
    return echelle, centre_x_monde, centre_y_monde


def monde_vers_ecran(x, y, echelle, cx, cy):
    ecran_x = LARGEUR / 2 + (x - cx) * echelle
    ecran_y = HAUTEUR / 2 - (y - cy) * echelle  # inversé : y monde vers le haut
    return ecran_x, ecran_y


def dessiner_voiture(surface, voiture, echelle, cx, cy, police):
    x, y = monde_vers_ecran(voiture.x_affiche, voiture.y_affiche, echelle, cx, cy)
    couleur = LISTE_COULEURS_RGB.get(voiture.couleur, (200, 200, 200))
    taille = 9

    # Triangle orienté dans la direction de la voiture (pointe vers l'avant).
    angle = radians(voiture.direction)
    pointe = (x + cos(angle) * taille, y - sin(angle) * taille)
    arriere_g = (x + cos(angle + 2.5) * taille, y - sin(angle + 2.5) * taille)
    arriere_d = (x + cos(angle - 2.5) * taille, y - sin(angle - 2.5) * taille)
    pygame.draw.polygon(surface, couleur, [pointe, arriere_g, arriere_d])
    pygame.draw.polygon(surface, (20, 20, 20), [pointe, arriere_g, arriere_d], width=1)

    # Étiquette : prénom + immatriculation.
    etiquette = police.render(f"{voiture.proprietaire} ({voiture.immatriculation})",
                               True, (230, 230, 230))
    surface.blit(etiquette, (x + 12, y - 8))

    # Jauge de carburant.
    ratio = max(voiture.reservoir / Voiture.CAPACITE_MAX, 0)
    pygame.draw.rect(surface, (70, 70, 70), (x + 12, y + 8, 40, 5))
    pygame.draw.rect(surface, (90, 200, 120), (x + 12, y + 8, 40 * ratio, 5))


def dessiner_hud(surface, police, nb_etapes):
    texte = police.render(
        f"Étapes simulées : {nb_etapes}   |   Échap ou fermer la fenêtre pour quitter",
        True, (180, 180, 180))
    surface.blit(texte, (10, HAUTEUR - 24))


def main():
    pygame.init()
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Simulation du garage")
    horloge = pygame.time.Clock()
    police = pygame.font.SysFont("consolas", 14)
    police_hud = pygame.font.SysFont("consolas", 13)

    garage = creer_garage(nb=8)
    nb_etapes = 0
    prochaine_etape_ms = pygame.time.get_ticks() + INTERVALLE_ETAPE_MS

    en_cours = True
    while en_cours:
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False
            elif evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_ESCAPE:
                en_cours = False

        maintenant = pygame.time.get_ticks()
        if maintenant >= prochaine_etape_ms:
            etape_aleatoire(garage)
            nb_etapes += 1
            prochaine_etape_ms = maintenant + INTERVALLE_ETAPE_MS

        for voiture in garage:
            voiture.maj_affichage()

        fenetre.fill((25, 25, 30))
        echelle, cx, cy = calculer_transformation(garage)
        for voiture in garage:
            dessiner_voiture(fenetre, voiture, echelle, cx, cy, police)
        dessiner_hud(fenetre, police_hud, nb_etapes)

        pygame.display.flip()
        horloge.tick(60)

    pygame.quit()

    print("\nÉtat final du garage :\n")
    for voiture in garage:
        print(str(voiture))


if __name__ == "__main__":
    main()