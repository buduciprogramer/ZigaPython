class Knjiga:
    def __init__(self, naslov, autor, godina_izdanja):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja
        self.dostupna = True

    def prikazi_informacije(self):
        print(f"Naslov: {self.naslov}")
        print(f"Autor: {self.autor}")
        print(f"Godina izdanja: {self.godina_izdanja}")
        print(f"Dostupna: {'Da' if self.dostupna else 'Ne'}\n")

    def iznajmi(self):
        if self.dostupna:
            self.dostupna = False
            print(f"Knjiga '{self.naslov}' je uspješno iznajmljena.")
        else:
            print(f"Knjiga '{self.naslov}' trenutno nije dostupna.")

    def vrati(self):
        self.dostupna = True
        print(f"Knjiga '{self.naslov}' je vraćena i sada je dostupna.")


class Osoba:
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime


class ClanBiblioteke(Osoba):
    def __init__(self, ime, prezime, broj_clanske_karte):
        super().__init__(ime, prezime)
        self.broj_clanske_karte = broj_clanske_karte
        self.lista_iznajmljenih_knjiga = []

    def iznajmi_knjigu(self, knjiga):
        if knjiga.dostupna:
            knjiga.iznajmi()
            self.lista_iznajmljenih_knjiga.append(knjiga)
        else:
            print(f"Knjiga '{knjiga.naslov}' nije dostupna za iznajmljivanje.")

    def vrati_knjigu(self, knjiga):
        if knjiga in self.lista_iznajmljenih_knjiga:
            knjiga.vrati()
            self.lista_iznajmljenih_knjiga.remove(knjiga)
        else:
            print(f"{self.ime} {self.prezime} nema iznajmljenu knjigu '{knjiga.naslov}'.")

    def prikazi_knjige(self):
        if not self.lista_iznajmljenih_knjiga:
            print(f"{self.ime} {self.prezime} trenutno nema iznajmljenih knjiga.")
        else:
            print(f"Knjige koje je iznajmio/la {self.ime} {self.prezime}:")
            for knjiga in self.lista_iznajmljenih_knjiga:
                print(f"- {knjiga.naslov} ({knjiga.autor}, {knjiga.godina_izdanja})")
        print()


def main():
    knjiga1 = Knjiga("Na Drini ćuprija", "Ivo Andrić", 1945)
    knjiga2 = Knjiga("Zločin i kazna", "Fjodor Dostojevski", 1866)
    knjiga3 = Knjiga("1984", "George Orwell", 1949)

    knjiga1.prikazi_informacije()
    knjiga2.prikazi_informacije()
    knjiga3.prikazi_informacije()

    clan1 = ClanBiblioteke("Ana", "Jurić", 1001)
    clan2 = ClanBiblioteke("Marko", "Horvat", 1002)

    clan1.iznajmi_knjigu(knjiga1)
    clan1.iznajmi_knjigu(knjiga2)
    clan2.iznajmi_knjigu(knjiga1)

    clan1.prikazi_knjige()
    clan2.prikazi_knjige()

    clan1.vrati_knjigu(knjiga1)
    clan2.iznajmi_knjigu(knjiga1)

    clan1.prikazi_knjige()
    clan2.prikazi_knjige()


if __name__ == "__main__":
    main()


