def caesar(message, decalage):
    if decalage >= 26:
        decalage = decalage % 26

    for letter in message:
        if ord(letter) >= 97 and ord(letter) <= 122: #minuscule
            if ord(letter) + decalage > 122:
                print(chr(ord(letter) + decalage - 26),end="")
            else:
                print(chr(ord(letter) + decalage), end="")
        elif ord(letter) >= 65 and ord(letter) <= 90: #majuscule
            if ord(letter) + decalage > 90:
                print(chr(ord(letter) + decalage - 26, end=""))
            else:
                print(chr(ord(letter) + decalage), end="")
        else:
            print(letter, end="")

caesar("toto, adore les burgers", 2)