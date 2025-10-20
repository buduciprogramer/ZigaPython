from abc import ABC, abstractmethod
import json

# Apstraktna klasa Knjiga
class Knjiga(ABC):
    def __init__(self, naslov, autor, godina_izdanja, dostupna=True):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja
        self.dostupna = dostupna

    @abstractmethod
    def prikazi_info(self):
        pass

    def iznajmi(self):
        if self.dostupna:
            self.dostupna = False
            return True
        else:
            return False

    def vrati(self):
        self.dostupna = True

# Izvedene klase

class Roman(Knjiga):
    def __init__(self, naslov, autor, godina_izdanja, zanr, dostupna=True):
        super().__init__(naslov, autor, godina_izdanja, dostupna)
        self.zanr = zanr

    def prikazi_info(self):
        status = "Dostupna" if self.dostupna else "Iznajmljena"
        print(f"Roman: {self.naslov}, autor: {self.autor}, godina: {self.godina_izdanja}, žanr: {self.zanr}, status: {status}")

class Udžbenik(Knjiga):
    def __init__(self, naslov, autor, godina_izdanja, predmet, dostupna=True):
        super().__init__(naslov, autor, godina_izdanja, dostupna)
        self.predmet = predmet

    def prikazi_info(self):
        status = "Dostupna" if self.dostupna else "Iznajmljena"
        print(f"Udžbenik: {self.naslov}, autor: {self.autor}, godina: {self.godina_izdanja}, predmet: {self.predmet}, status: {status}")

class Strip(Knjiga):
    def __init__(self, naslov, autor, godina_izdanja, ilustrator, dostupna=True):
        super().__init__(naslov, autor, godina_izdanja, dostupna)
        self.ilustrator = ilustrator

    def prikazi_info(self):
        status = "Dostupna" if self.dostupna else "Iznajmljena"
        print(f"Strip: {self.naslov}, autor: {self.autor}, godina: {self.godina_izdanja}, ilustrator: {self.ilustrator}, status: {status}")

# Klasa ClanBiblioteke

class ClanBiblioteke:
    def __init__(self, ime, prezime, clanski_broj):
        self.ime = ime
        self.prezime = prezime
        self.clanski_broj = clanski_broj
        self.lista_knjiga = []

    def iznajmi_knjigu(self, knjiga):
        if knjiga.iznajmi():
            self.lista_knjiga.append(knjiga)
            print(f"Knjiga '{knjiga.naslov}' je uspešno iznajmljena članu {self.ime} {self.prezime}.")
        else:
            print(f"Knjiga '{knjiga.naslov}' trenutno nije dostupna za iznajmljivanje.")

    def vrati_knjigu(self, knjiga):
        if knjiga in self.lista_knjiga:
            knjiga.vrati()
            self.lista_knjiga.remove(knjiga)
            print(f"Knjiga '{knjiga.naslov}' je vraćena.")
        else:
            print(f"Član nema tu knjigu u iznajmljenim knjigama.")

    def prikazi_knjige(self):
        if not self.lista_knjiga:
            print(f"Član {self.ime} {self.prezime} nema trenutno iznajmljenih knjiga.")
        else:
            print(f"Knjige koje je član {self.ime} {self.prezime} iznajmio:")
            for knjiga in self.lista_knjiga:
                knjiga.prikazi_info()

# Klasa Biblioteka

class Biblioteka:
    def __init__(self, naziv):
        self.naziv = naziv
        self.knjige = []
        self.clanovi = []

    def dodaj_knjigu(self, knjiga):
        self.knjige.append(knjiga)
        print(f"Dodata knjiga '{knjiga.naslov}' u biblioteku.")

    def dodaj_clana(self, clan):
        self.clanovi.append(clan)
        print(f"Dodat član {clan.ime} {clan.prezime} sa brojem {clan.clanski_broj}.")

    def prikazi_dostupne_knjige(self):
        dostupne = [k for k in self.knjige if k.dostupna]
        if not dostupne:
            print("Nema dostupnih knjiga u biblioteci.")
        else:
            print("Dostupne knjige:")
            for knjiga in dostupne:
                knjiga.prikazi_info()

    def prikazi_clanove(self):
        if not self.clanovi:
            print("Nema članova biblioteke.")
        else:
            print("Članovi biblioteke:")
            for clan in self.clanovi:
                print(f"{clan.clanski_broj}: {clan.ime} {clan.prezime}")

    def pretrazi_po_autoru(self, autor):
        pronadjene = [k for k in self.knjige if k.autor.lower() == autor.lower()]
        if not pronadjene:
            print(f"Nema knjiga autora {autor}.")
        else:
            print(f"Knjige autora {autor}:")
            for knjiga in pronadjene:
                knjiga.prikazi_info()

    def sacuvaj_podatke(self, filename="biblioteka_podaci.json"):
        data = {
            "knjige": [],
            "clanovi": []
        }

        for knjiga in self.knjige:
            tip = knjiga.__class__.__name__
            knjiga_dict = {
                "tip": tip,
                "naslov": knjiga.naslov,
                "autor": knjiga.autor,
                "godina_izdanja": knjiga.godina_izdanja,
                "dostupna": knjiga.dostupna,
            }
            if tip == "Roman":
                knjiga_dict["zanr"] = knjiga.zanr
            elif tip == "Udžbenik":
                knjiga_dict["predmet"] = knjiga.predmet
            elif tip == "Strip":
                knjiga_dict["ilustrator"] = knjiga.ilustrator

            data["knjige"].append(knjiga_dict)

        for clan in self.clanovi:
            clan_dict = {
                "ime": clan.ime,
                "prezime": clan.prezime,
                "clanski_broj": clan.clanski_broj,
                "lista_knjiga": [k.naslov for k in clan.lista_knjiga]
            }
            data["clanovi"].append(clan_dict)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Podaci su sačuvani u fajl '{filename}'.")

    def ucitaj_podatke(self, filename="biblioteka_podaci.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("Fajl sa podacima ne postoji.")
            return

        self.knjige = []
        self.clanovi = []

        for k in data.get("knjige", []):
            tip = k.get("tip")
            if tip == "Roman":
                knjiga = Roman(k["naslov"], k["autor"], k["godina_izdanja"], k["zanr"], k["dostupna"])
            elif tip == "Udžbenik":
                knjiga = Udžbenik(k["naslov"], k["autor"], k["godina_izdanja"], k["predmet"], k["dostupna"])
            elif tip == "Strip":
                knjiga = Strip(k["naslov"], k["autor"], k["godina_izdanja"], k["ilustrator"], k["dostupna"])
            else:
                continue
            self.knjige.append(knjiga)

        for c in data.get("clanovi", []):
            clan = ClanBiblioteke(c["ime"], c["prezime"], c["clanski_broj"])
            # Poveži knjige prema naslovu iz biblioteke
            for naslov_knjige in c.get("lista_knjiga", []):
                knjiga = next((k for k in self.knjige if k.naslov == naslov_knjige), None)
                if knjiga:
                    clan.lista_knjiga.append(knjiga)
                    knjiga.dostupna = False
            self.clanovi.append(clan)
        print(f"Podaci su učitani iz fajla '{filename}'.")

# Glavni program

def meni():
    print("\n--- Meni biblioteke ---")
    print("1. Prikaži dostupne knjige")
    print("2. Iznajmi knjigu")
    print("3. Vrati knjigu")
    print("4. Dodaj novog člana")
    print("5. Prikaži članove")
    print("6. Pretraži knjige po autoru")
    print("7. Sačuvaj stanje biblioteke")
    print("8. Učitaj stanje biblioteke")
    print("0. Izlaz")

def pronadji_clana(biblioteka, broj):
    return next((c for c in biblioteka.clanovi if c.clanski_broj == broj), None)

def pronadji_knjigu(biblioteka, naslov):
    return next((k for k in biblioteka.knjige if k.naslov.lower() == naslov.lower()), None)

def main():
    biblioteka = Biblioteka("Narodna biblioteka")

    # Dodavanje nekoliko knjiga
    biblioteka.dodaj_knjigu(Roman("Na Drini ćuprija", "Ivo Andrić", 1945, "istorijski"))
    biblioteka.dodaj_knjigu(Udžbenik("Matematika 1", "Petar Petrović", 2010, "matematika"))
    biblioteka.dodaj_knjigu(Strip("Alan Ford", "Tiziano Sclavi", 1969, "Roberto Raviola"))

    # Dodavanje članova
    biblioteka.dodaj_clana(ClanBiblioteke("Marko", "Marković", 1))
    biblioteka.dodaj_clana(ClanBiblioteke("Jelena", "Jovanović", 2))
    biblioteka.dodaj_clana(ClanBiblioteke("Haso","Hasić",3))

    while True:
        meni()
        izbor = input("Izaberi opciju: ")

        if izbor == "1":
            biblioteka.prikazi_dostupne_knjige()
        elif izbor == "2":
            broj = int(input("Unesi članski broj: "))
            clan = pronadji_clana(biblioteka, broj)
            if not clan:
                print("Član nije pronađen.")
                continue
            naslov = input("Unesi naslov knjige: ")
            knjiga = pronadji_knjigu(biblioteka, naslov)
            if knjiga:
                clan.iznajmi_knjigu(knjiga)
            else:
                print("Knjiga nije pronađena.")
        elif izbor == "3":
            broj = int(input("Unesi članski broj: "))
            clan = pronadji_clana(biblioteka, broj)
            if not clan:
                print("Član nije pronađen.")
                continue
            naslov = input("Unesi naslov knjige: ")
            knjiga = pronadji_knjigu(biblioteka, naslov)
            if knjiga:
                clan.vrati_knjigu(knjiga)
            else:
                print("Knjiga nije pronađena.")
        elif izbor == "4":
            ime = input("Unesi ime: ")
            prezime = input("Unesi prezime: ")
            broj = int(input("Unesi članski broj: "))
            if pronadji_clana(biblioteka, broj):
                print("Članski broj već postoji.")
            else:
                biblioteka.dodaj_clana(ClanBiblioteke(ime, prezime, broj))
        elif izbor == "5":
            biblioteka.prikazi_clanove()
        elif izbor == "6":
            autor = input("Unesi ime autora: ")
            biblioteka.pretrazi_po_autoru(autor)
        elif izbor == "7":
            biblioteka.sacuvaj_podatke()
        elif izbor == "8":
            biblioteka.ucitaj_podatke()
        elif izbor == "0":
            print("Izlaz iz programa.")
            break
        else:
            print("Nepoznata opcija. Pokušajte ponovo.")


if __name__ == "__main__":
    main()