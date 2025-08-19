moj_rjecnik = {}

while True:
    # Unos ključa
    kljuc = input("Unesi ključ (ili 'kraj' za završetak): ")
    if kljuc.lower() == 'kraj':
        break

    # Unos dviju vrijednosti za taj ključ
    vrijednost1 = input(f"Unesi prvu vrijednost za ključ '{kljuc}': ")
    vrijednost2 = input(f"Unesi drugu vrijednost za ključ '{kljuc}': ")

    # Dodavanje u rječnik
    moj_rjecnik[kljuc] = [vrijednost1, vrijednost2]

# Ispis konačnog rječnika
print("\nKonačni rječnik:")
for k, v in moj_rjecnik.items():
    print(f"{k}: {v}")