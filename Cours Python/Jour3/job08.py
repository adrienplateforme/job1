a = float(input("Entrez la longueur a : "))
b = float(input("Entrez la longueur b : "))
c = float(input("Entrez la longueur c : "))

if a > b:
    a, b = b, a

if a > c:
    a, c = c, a

if b > c:
    b, c = c, b

equilateral = a == b and b == c
isocele = a == b or b == c
rectangle = abs(a * a + b * b - c * c) < 0.03

if a + b > c:
    if equilateral:
        print("Vous avez un triangle équilateral.")
    elif isocele and rectangle:
        print("Vous avez un triangle isocèle rectangle.")
    elif isocele:
        print("Vous avez un triangle isocèle.")
    elif rectangle:
        print("Vous avez un triangle rectangle.")
    else:
        print("Vous avez un triangle quelconque.")
else:
    print("Vous n'avez pas de triangle.")