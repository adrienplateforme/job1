L =  [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
i = 0
x = 0
y = 1

for a in L:
    i = i + 1

while x < i - 1:
    if y < i and L[x] == L[y]:
        del L[y]
        i = i - 1
    elif y < i:
        y = y + 1
    else:
        x = x + 1
        y = x + 1

print(L)