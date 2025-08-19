broj = int(input("Unesite cijeli broj: "))

# Dobavljanje zadnje cifre
zadnja_cifra = abs(broj) % 10  # Koristimo abs da broj može biti i negativan

# Provjera djeljivosti
if zadnja_cifra % 3 == 0:
    print(f"Zadnja cifra broja je {zadnja_cifra} i djeljiva je sa 3.")
else:
    print(f"Zadnja cifra broja je {zadnja_cifra} i NIJE djeljiva sa 3.")