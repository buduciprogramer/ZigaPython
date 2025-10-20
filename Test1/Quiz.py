class Pitanje:
    def __init__(self, tekst_pitanja, opcije, tacan_odgovor):
        self.tekst_pitanja = tekst_pitanja
        self.opcije = opcije
        self.tacan_odgovor = tacan_odgovor.upper()

    def provjeri_odgovor(self, odgovor):
        return odgovor.upper() == self.tacan_odgovor


class Kviz:
    def __init__(self, lista_pitanja):
        self.lista_pitanja = lista_pitanja
        self.broj_poena = 0

    def pokreni_kviz(self):
        self.broj_poena = 0
        broj_tacnih = 0
        uzastopne_greske = 0

        print("Dobrodošao/la u kviz! Odgovori birajući A, B, C ili D.\n")

        for i, pitanje in enumerate(self.lista_pitanja, start=1):
            print(f"Pitanje {i}: {pitanje.tekst_pitanja}")
            for opcija in pitanje.opcije:
                print(opcija)

            odgovor = input("Tvoj odgovor (A/B/C/D): ").upper()

            while odgovor not in ['A', 'B', 'C', 'D']:
                odgovor = input("Nevažeći unos. Pokušaj ponovo (A/B/C/D): ").upper()

            if pitanje.provjeri_odgovor(odgovor):
                print("Tačno!\n")
                self.broj_poena += 1
                broj_tacnih += 1
                uzastopne_greske = 0
            else:
                print(f" Netočno! Tačan odgovor je: {pitanje.tacan_odgovor}\n")
                self.broj_poena -= 1
                uzastopne_greske += 1

            if uzastopne_greske == 3:
                print("Tri uzastopne greške. Kviz je prekinut.\n")
                break

        self.rezultat(broj_tacnih, i)

    def rezultat(self, broj_tacnih, ukupno_pitanja):
        print("Kraj kviza!")
        print(f"Osvojeni poeni: {self.broj_poena}")
        postotak = (broj_tacnih / ukupno_pitanja) * 100
        print(f"Tačnost: {postotak:.2f}% ({broj_tacnih}/{ukupno_pitanja})")


# -----------------------------
# Glavni program
# -----------------------------

def main():
    pitanja = [
        Pitanje(
            "Ko je napisao 'Na Drini ćuprija'?",
            ["A. Ivo Andrić", "B. Meša Selimović", "C. Branko Ćopić", "D. Miroslav Krleža"],
            "A"
        ),
        Pitanje(
            "Koja godina je početak Prvog svjetskog rata?",
            ["A. 1912", "B. 1914", "C. 1918", "D. 1920"],
            "B"
        ),
        Pitanje(
            "Šta označava CPU u računaru?",
            ["A. Central Process Unit", "B. Computer Primary Unit", "C. Central Processing Unit", "D. Core Performance Unit"],
            "C"
        ),
        Pitanje(
            "Koja je prijestolnica Francuske?",
            ["A. Rim", "B. Madrid", "C. Pariz", "D. Berlin"],
            "C"
        ),
        Pitanje(
            "Koliko kontinenata postoji?",
            ["A. 5", "B. 6", "C. 7", "D. 8"],
            "C"
        )
    ]

    moj_kviz = Kviz(pitanja)
    moj_kviz.pokreni_kviz()


if __name__ == "__main__":
    main()
