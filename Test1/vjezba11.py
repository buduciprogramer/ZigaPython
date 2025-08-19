matrica = []

# Unos elemenata matrice 4x4
print("Unesite elemente matrice 4x4:")
for i in range(4):
    red = []
    for j in range(4):
        element = int(input(f"Element [{i+1},{j+1}]: "))
        red.append(element)
    matrica.append(red)

# Brojanje pozitivnih elemenata
broj_pozitivnih = 0
for red in matrica:
    for element in red:
        if element > 0:
            broj_pozitivnih += 1

# Ispis rezultata
print(f"Broj pozitivnih elemenata u matrici je: {broj_pozitivnih}")