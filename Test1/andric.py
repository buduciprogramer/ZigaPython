biblioteka = {}

n = int(input("Unesite broj autora: "))

for _ in range(n):
    autor = input("Unesite ime autora: ").strip().lower()
    djela = input("Unesite djela autora (odvojena zarezom): ").split(',')
    # Uklanjanje suvišnih razmaka i spremanje u rječnik
    biblioteka[autor] = [djelo.strip() for djelo in djela]

# Pretraga autora "andric"
trazeni_autor = "andric"

if trazeni_autor in biblioteka:
    print(f"Djela autora '{trazeni_autor}':")
    for djelo in biblioteka[trazeni_autor]:
        print("-", djelo)
else:
    print("Nema traženog autora.")