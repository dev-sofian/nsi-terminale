from compte import Compte


class Client:
    def __init__(self, n: str, p: str):
        self.nom = n
        self.prenom = p
        # le compte 0 est non rémunéré, le 1 est rémunéré
        self.comptes = []

    def get_identite(self) -> str:
        """
        accesseur identité

        Returns:
            str: nom prénom
        """
        return self.nom + " " + self.prenom

    def get_comptes(self) -> list:
        """
        accesseur des comptes

        Returns:
            list: liste des comptes
        """
        return self.comptes

    def ajouter_compte(self, num_compte: int, remunere: bool) -> None:
        """
        Crée un nouveau compte

        Args:
            num_compte (int): numéro du compte créé
            remunere (bool): type de compte
        """
        if remunere == False:
            self.comptes.append(Compte(num_compte, remunere))
        elif remunere == True:
            self.comptes.append(Compte(num_compte, remunere))
        return self.comptes

    def crediter_argent(self, somme: int, type_compte: bool) -> None:
        """
        ajouter l'argent sur le compte courant ou épargne

        Args:
            somme (int): somme créditée
            type_compte (bool): type de compte
        """
        if type_compte == False:
            self.comptes[0].crediter(somme)
        else:
            self.comptes[1].crediter(somme)

    def debiter_argent(self, somme: int, type_compte: bool) -> bool:
        """
        retirer l'argent sur le compte courant ou épargne

        Args:
            somme (int): somme débitée
            type_compte (bool): type de compte

        Returns:
            bool: True si le compte a été débité
        """
        if type_compte == False:
            return self.comptes[0].debiter(somme)
        else:
            return self.comptes[1].debiter(somme)

    def afficher(self) -> str:
        """
        description du client

        Returns:
            str: texte descriptif
        """
        texte = self.nom + " " + self.prenom + "\n"
        for compte in self.comptes:
            texte = texte + compte.afficher()
        return texte
