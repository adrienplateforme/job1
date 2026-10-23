a = ["Senzo", "David", "Adri"]

print(a[1])

Senzo = 2
David = True
Adri = "moi"

b = [Senzo, David, Adri]

for prenom in b:
    print(prenom)

test = 0
while test < len(b):
    print(b[test])
    test = test + 1


c = {
    "Senzo": 2,
    "David": True,
    "Adri": "moi"
}
print(c["Senzo"])

d = [a, b, c]
print(d[1][1])