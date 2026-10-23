def moyenne(a, b, c):
    return (a + b + c ) / 3

a, b, c = map(int, input("Rentrez vos trois notes séparées d'un espace : ").split())

moyenne_etudiant = moyenne(a,b,c)
if moyenne_etudiant >= 15:
    print("Très bon élève")
elif moyenne_etudiant >= 11:
    print("Bon élève")
elif moyenne_etudiant >= 8:
    print("Élève moyen")
else:
    print("Élève devant faire des efforts")