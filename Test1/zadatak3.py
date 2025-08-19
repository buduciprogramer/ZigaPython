def validno_ime_ili_prezime(tekst):
    return tekst.isalpha()

def validan_broj(tekst):
    return tekst.isdigit()

ime=input("Unesite vaše ime")
prezime=input("Unesite vaše prezime")
broj_telefona = input("Unesite broj telefona: ")


if validno_ime_ili_prezime(ime) and validno_ime_ili_prezime(prezime) and validan_broj(broj_telefona):
    print("\nUnos je validan.")
    print(f"Ime: {ime}")
    print(f"Prezime: {prezime}")
    print(f"Broj telefona: {broj_telefona}")
else:
    print("\nUnos nije validan!")
    if not validno_ime_ili_prezime(ime):
        print("- Ime mora sadržavati samo slova.")
    if not validno_ime_ili_prezime(prezime):
        print("- Prezime mora sadržavati samo slova (bez razmaka ili brojeva).")
    if not validan_broj(broj_telefona):
        print("- Broj telefona mora sadržavati samo cifre.")

