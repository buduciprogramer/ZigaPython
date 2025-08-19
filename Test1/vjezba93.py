drzave = {
    "++381": "Srbija",
    "++385": "Hrvatska",
    "++387": "Bosna i Hercegovina",
    "++386": "Slovenija",
    "++389": "Severna Makedonija",
    "++382": "Crna Gora",
    "++1": "Amerika"
}

telefon = input("Unesi broj telefona (npr. ++381-63-1234567): ")
djelovi = telefon.split("-")

if len(djelovi) == 3:
    pozivni = djelovi[0]
    mreza = djelovi[1]
    broj = djelovi[2]

    drzava = drzave.get(pozivni, "Nepoznata država")

    print("Država:", drzava)
    print("Pozivni broj:", pozivni)
    print("Mreža:", mreza)
    print("Broj:", broj)
else:
    print("Greška: format nije ispravan. Pokušaj ponovo.")