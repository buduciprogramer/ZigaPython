import string

# Unos stringa od korisnika
tekst = input("Unesi tekst za provjeru: ")

# Pretvaranje u mala slova i uklanjanje razmaka i interpunkcije
ocisceni_tekst = ''.join(char.lower() for char in tekst if char.isalnum())

# Provjera da li je string palindrom
if ocisceni_tekst == ocisceni_tekst[::-1]:
    print("Uneseni tekst je palindrom.")
else:
    print("Uneseni tekst nije palindrom.")