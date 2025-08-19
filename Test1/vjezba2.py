x = int(input("Unesite cijeli broj (manji ili jednak 180): "))

# Provjera da li je broj manji ili jednak 180
if x > 180:
    print("Broj mora biti manji ili jednak 180.")
else:
    print(f"Brojevi od {x} do 180 koji su djeljivi s 5, ali nisu djeljivi s 15:")
    for i in range(x, 181):
        if i % 5 == 0 and i % 15 != 0:
            print(i, end=" ")