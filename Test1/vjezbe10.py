def unos_podataka():
    broj_studenata = int(input("Unesite broj studenata: "))
    studenti = {}

    for _ in range(broj_studenata):
        ime = input("Unesite ime studenta: ")
        prisustvo_str = input("Unesite prisustvo po nedjeljama (0 ili 1, odvojeno zarezima): ")
        prisustvo_lista = [int(x) for x in prisustvo_str.split(",")]
        studenti[ime] = prisustvo_lista

    return studenti

def izracunaj_procenat(prisustvo_lista):
    ukupno = len(prisustvo_lista)
    prisutan = sum(prisustvo_lista)
    return (prisutan / ukupno) * 100 if ukupno > 0 else 0

def statistika(studenti):
    procenti = {}
    max_prisustvo = -1
    najbolji_student = ""
    suma_procenata = 0
    manje_od_50 = []

    for ime, prisustvo in studenti.items():
        procenat = izracunaj_procenat(prisustvo)
        procenti[ime] = procenat
        suma_procenata += procenat

        if procenat > max_prisustvo:
            max_prisustvo = procenat
            najbolji_student = ime

        if procenat < 50:
            manje_od_50.append(ime)

    prosjek = suma_procenata / len(studenti) if studenti else 0

    return procenti, najbolji_student, max_prisustvo, prosjek, manje_od_50

def prikazi_rezultate(procenti, najbolji_student, max_prisustvo, prosjek, manje_od_50):
    print("\n--- Prisustvo po studentima (%):")
    for ime, procenat in procenti.items():
        print(f"{ime}: {procenat:.2f}%")

    print(f"\n Student sa najvećim prisustvom: {najbolji_student} ({max_prisustvo:.2f}%)")
    print(f" Prosječno prisustvo grupe: {prosjek:.2f}%")

    if manje_od_50:
        print("\n Studenti sa manje od 50% prisustva:")
        for ime in manje_od_50:
            print(f"- {ime}")
    else:
        print("\n Nema studenata sa manje od 50% prisustva.")

def main():
    studenti = unos_podataka()
    procenti, najbolji, max_proc, prosjek, slabiji = statistika(studenti)
    prikazi_rezultate(procenti, najbolji, max_proc, prosjek, slabiji)

# Pokretanje programa
main()