from client import Client
from datetime import date


class Banque:
    def __init__(self):
        self.clients = []
        self.remuneration = 0.03
        self.numero_libre = 0

    def donner_numero_compte(self) -> int:
        """
        donne un numéro de compte non déjà attribué

        Returns:
            int: numéro libre
        """
        self.numero_libre = self.numero_libre + 1
        return self.numero_libre

    def creer_client(self, nom: str, prenom: str) -> None:
        """
        crée un nouveau client et ses comptes

        Args:
            nom (str): nom du client
            prenom (str): prénom du client
        """
        n = self.numero_libre
        client= Client(nom, prenom)
        client.ajouter_compte(n, False)
        client.ajouter_compte(n, True)
        self.clients.append(client)
        self.donner_numero_compte()


    def appliquer_taux(self) -> None:
        """
        applique le taux de rémunération sur tous les comptes épargnes
        """
        for i in range(len(self.clients)):
            self.clients[i].comptes[1].somme *= (1+self.remuneration)
            

    def chercher_client(self, identite: str) -> Client:
        """
        trouve le client par son nom prénom

        Args:
            identite (str): nom prénom du client

        Returns:
            Client: le Client trouvé ou None
        """
        for i in range(len(self.clients)):
            if self.clients[i].get_identite() == identite:
                return self.clients[i]
        return None
