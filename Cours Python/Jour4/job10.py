def verif(a):
    if isinstance(a, int):
        if a == 0:
            return("Votre nombre est nul")
        elif a < 0:
            return("Votre nombre est négatif")
        elif a % 2 == 0:
            return("Votre nombre est pair")
        elif a % 2 != 0:
            return("Votre nombre est impair")
    else:
        return("Veuillez rentrez un nombre entier positif")

print(verif(5))
print(verif(-6))
print(verif(0))
print(verif("x"))