def broj_pozitivnih():
    # 1. Automatska lista brojeva
    lista = [-5, 3, 0, 7, -2, 10, -1]

    # 2. Ispis liste
    print("Lista brojeva:")
    for broj in lista:
        print(broj, end=' ')
    print()  # novi red

    # 3. Prebrojavanje pozitivnih
    brojac = 0
    for broj in lista:
        if broj > 0:
            brojac += 1

    # 4. Ispis rezultata
    print("Ukupno pozitivnih brojeva:", brojac)

# Poziv funkcije
broj_pozitivnih()