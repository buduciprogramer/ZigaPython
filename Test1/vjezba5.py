pokusaji = 0

while pokusaji < 4:
    sifra = input("Unesite šifru (4 cifre): ")

    # Provjera: da li je šifra tačno 4 cifre i da li su sve cifre
    if len(sifra) == 4 and sifra.isdigit():
        print("Dobrodošli na Vaš račun.")
        break
    else:
        pokusaji += 1
        if pokusaji == 4:
            print("Blokirani ste s Vašeg računa.")
        else:
            print(f"Neispravna šifra. Pokušajte ponovo. Preostalo pokušaja: {4 - pokusaji}")