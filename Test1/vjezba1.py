tekst = input("Unesite neki tekst: ")

# Provjera da li sadrži riječ 'python'
if "python" in tekst.lower():
    # Zamjena svih pojavljivanja 'python' bez obzira na veliko/malo slovo
    tekst_novi = tekst.replace("python", "programski jezik opće namjene visoke razine")
    tekst_novi = tekst_novi.replace("Python", "programski jezik opće namjene visoke razine")
    print("Rezultat:\n", tekst_novi)
else:
    print("Nema traženog pojma.")