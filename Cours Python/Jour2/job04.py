nombre_max = int(input("Entrez un entier supérieur à zéro (N) :"))
i = 1
table = 1

print("Table de multiplication de", table, ":")
while table <= nombre_max:
    print(table, "x", i, "=", i * table)
    i = i + 1
    if i == 11:
        i = 1
        table = table + 1
        if table <= nombre_max:
            print("\nTable de multiplication de", table, ":")