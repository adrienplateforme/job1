montant = 20000
taux = 5
gain = montant * taux / 100
print("Gain annuel pour 20k€ avec un taux de 5%:", gain,"€")

taux = taux + 2
montant = montant + 5000
gain = montant * taux / 100
print("Gain annuel pour 25k€ avec un taux de 7%", gain,"€")

taux = taux - 1
montant = montant * 0.9
gain = montant * taux / 100
print("Gain annuel pour", montant,"€ avec un taux a 6%", gain,"€")