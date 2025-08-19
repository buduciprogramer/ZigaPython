plate = {}  # prazan rečnik

# unos podataka
for i in range(5):
    ime = input(f"Unesi ime osobe {i+1}: ")
    plata = float(input(f"Unesi platu za {ime}: "))
    plate[ime] = plata

# računanje sume i proseka
ukupno = sum(plate.values())
prosek = ukupno / len(plate)

# ispis rezultata
print(f"Suma svih plata je: {ukupno}")
print(f"Prosječna plata je: {prosek}")