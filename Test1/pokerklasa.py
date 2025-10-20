import random

class Karta:
    znakovi = ['♠', '♥', '♦', '♣']
    vrijednosti = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    def __init__(self, vrijednost, znak):
        self.vrijednost = vrijednost
        self.znak = znak
        
    def __repr__(self):
        return f"{self.vrijednost}{self.znak}"    

class Spil:
    def __init__(self):
        self.karte = [Karta(v, z) for z in Karta.znakovi for v in Karta.vrijednosti]
        self.promjesaj()
         
    def promjesaj(self):
        random.shuffle(self.karte)
        
    def podijeli(self, broj=1):
        return [self.karte.pop() for _ in range(broj)]

class PokerRuka:
    def __init__(self, karte):
        self.karte = karte

    def __repr__(self):
        return " ".join(str(k) for k in self.karte)

    def ocijeni(self):
        return "Nije implementirano"

class PokerIgra:
    def __init__(self, broj_igraca=2):
        self.spil = Spil()
        self.broj_igraca = broj_igraca
        self.ruke = []

    def zapocni(self):
        print(" Dijeljenje karata...")
        for _ in range(self.broj_igraca):
            ruka = PokerRuka(self.spil.podijeli(2))
            self.ruke.append(ruka)
        
        print("\n Ruke igrača:")
        for i, ruka in enumerate(self.ruke, 1):
            print(f"Igrač {i}: {ruka}")
        
        self.flop = self.spil.podijeli(3)
        self.turn = self.spil.podijeli(1)
        self.river = self.spil.podijeli(1)

        print("\n🃍 Zajedničke karte:")
        print(f"Flop: {self.flop}")
        print(f"Turn: {self.turn}")
        print(f"River: {self.river}")

if __name__ == "__main__":
    igra = PokerIgra(broj_igraca=2)
    igra.zapocni()
          