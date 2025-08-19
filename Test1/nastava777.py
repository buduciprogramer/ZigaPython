ocjene = []
for i in range(8):
    ocjena = input(f"Unesite ocjenu broj {i+1}: ")
    while not ocjena.replace('.', '', 1).isdigit() or not (1 <= float(ocjena) <= 5):
        print("Pogrešan unos. Ocjena mora biti broj između 1 i 5.")
        ocjena = input(f"Ponovo unesite ocjenu broj {i+1}: ")
    ocjene.append(float(ocjena))
prosjek = sum(ocjene) / len(ocjene)
print(f"\nProsjek ocjena je: {prosjek:.2f}")
if prosjek >= 4.5:
    print("Uspjeh: Odličan")
elif 3.5 <= prosjek < 4.5: print("Uspjeh:vrlodobar")

else:
    ("Uspjeh dobar")