def time_to_text(a):
    if type(a) == int and a > 0:

        hcut = a // 60
        y = a % 60

        match hcut:
            case 0,1:
                unite_heure = "heure"
            case _:
                unite_heure = "heures"

        match y:
            case 0,1:
                unite_minute = "minute"
            case _:
                unite_minute = "minutes"

        print(f"{hcut} {unite_heure} et {y} {unite_minute}")
    else:
        print("Veuillez entrer un nombre entier positif")