L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
mini = L[0]
maxi = L[0]

for x in L:

    if x < mini:
        mini = x
    if x > maxi:
        maxi = x

print(f"la valeur max est : {maxi}\nla valeur min est : {mini}")