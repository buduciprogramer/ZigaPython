n = int(input("Unesite cijeli broj: "))

if n < 0:
    print("Molimo unesite pozitivan cijeli broj")
else:
    proizvod = 1
    for i in range(1, n + 1):
        proizvod *= i
    print(f"Proizvod svih brojeva od 1 do {n} je: {proizvod}")