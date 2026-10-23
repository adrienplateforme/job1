L = [2, 3, 5, 4, 8, 7, 1, 9, 6]
x = 0
i = 0

for a in L:
    i = i + 1 #on cherche la longueur max de la liste important pour ne pas en sortir

while x < i - 1:
    y = x + 1

    while y < i:# i commence pas à 0, y oui!!!! cad y==i sort de la liste
        if L[y] < L[x]:
            temp = L[x]
            L[x] = L[y]
            L[y] = temp
        y = y + 1

    x = x + 1

print(L)