from banque import Banque

# créer la banque du périgord
banque_perigord = Banque()

# créer 2 clients
banque_perigord.creer_client("Viroulaud", "Christophe")
banque_perigord.creer_client("Macron", "Emmanuel")

# créditer le compte courant de Viroulaud de 500€
viroulaud = banque_perigord.chercher_client("Viroulaud Christophe")
viroulaud.crediter_argent(500.0, False)
# créditer le compte épargne de Viroulaud de 1000€
viroulaud.crediter_argent(1000.0, True)

# afficher les comptes de Viroulaud
print(viroulaud.afficher())

# rémunérer
banque_perigord.appliquer_taux()

# afficher les comptes de Viroulaud
print(viroulaud.afficher())
