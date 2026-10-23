def my_long_word(taille, texte):
    texte = texte.replace(",", "")
    mots = texte.split()

    for mot in mots:
        i = 0
        for lettres in mot:
            i = i + 1
        if i > taille:
            print(mot, end=" ")

my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance")