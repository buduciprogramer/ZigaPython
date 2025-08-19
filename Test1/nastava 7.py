lista = []

# Unos 5 elemenata
for i in range(5):
    broj = int(input(f"Unesite {i+1}. broj: "))
    lista.append(broj)

# Računanje proizvoda
proizvod = 1
for broj in lista:
    proizvod *= broj

print(f"\nUnesena lista: {lista}")
print(f"Proizvod svih elemenata je: {proizvod}")