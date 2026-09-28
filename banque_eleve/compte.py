class Compte:
    def __init__(self, num: int, remunere: bool):
        self.num_compte = num
        self.somme = 0
        self.est_remunere = remunere

    def get_somme(self) -> float:
        """
        accesseur de somme  

        Returns:
            float: la somme sur le compte
        """
        return float(self.somme)

    def set_somme(self, s: float) -> None:
        """
        mutateur somme

        Params:
            s (float): valeur à mettre à la place
        """
        self.somme = s

    def verif_remunere(self) -> bool:
        """
        accesseur est_remunere

        Returns:
            bool: True si compte rémunéré
        """
        if self.est_remunere:
            return True
        return False

    def crediter(self, s: float) -> None:
        """
        crédite le compte

        Args:
            s (float): la somme à créditer
        """
        self.somme += s

    def debiter(self, s: float) -> bool:
        """
        débite le compte si possible

        Args:
            s (float): la somme à débiter

        Returns:
            bool: True si le compte a été débité
        """
        if self.somme - s < 0:
            return False
        else:
            self.somme -= s
            return True

    def afficher(self) -> str:
        """
        description du compte

        Returns:
            str: texte descriptif
        """
        texte = "compte n°" + str(self.num_compte) + "\n"
        if self.est_remunere:
            texte = texte + "compte épargne \n"
        else:
            texte = texte + "compte courant \n"
        texte = texte + "solde: " + str(self.somme) + "€ \n"
        return texte
