L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
i = 0

for fl in L:
    entier = int(fl)
    deci = fl - entier
    if deci >= 0.5:
        L[i] = int(fl + 1)
    else:
        L[i] = int(fl)
    i = i + 1

#Copié collé de l'exo 12 OKLM
x = 0
i = 0

for a in L:
    i = i + 1

while x < i - 1:
    y = x + 1

    while y < i:
        if L[y] < L[x]:
            temp = L[x]
            L[x] = L[y]
            L[y] = temp
        y = y + 1

    x = x + 1
print(L)