nom= "Baguette Kebab"
prix= 0.5
stock= 30
print("Nom :", nom, "| Prix unitaire :", prix, "€ | Stock :", stock)
commande = int(input("Combien de baguettes voulez-vous commander ? Attention chaque achat augmente le prix de 10% "))
if commande > 0:
    stock = stock - commande
    prix = prix * 1.10
print("Nouveaux stock de", nom,":", stock," | Nouveaux prix de", nom,":", prix)