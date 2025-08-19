import random

def prazna_tabla():
    return [[0 for _ in range(9)] for _ in range(9)]

def legalan_broj(tabla, broj, red, kolona):
    if broj in tabla[red]:
        return False
    
    for i in range(9):
        if tabla[i][kolona] == broj:
            return False
        
    poc_red = red - red % 3
    poc_kol = kolona - kolona % 3
    
    for i in range(3):
        for j in range(3):
            if tabla[poc_red + i][poc_kol + j] == broj:
                return False

    return True

def popuni_tabelu(tabla):
    for red in range(9):
        for kolona in range(9):
            if tabla[red][kolona] == 0:
                brojevi = list(range(1, 10))
                random.shuffle(brojevi)
                for broj in brojevi:
                    if legalan_broj(tabla, broj, red, kolona):
                        tabla[red][kolona] = broj
                        if popuni_tabelu(tabla):
                            return True
                        tabla[red][kolona] = 0
                return False
    return True

def ukloni_polja(tabla, broj_za_ukloniti=36):
    uklonjeno = 0
    while uklonjeno < broj_za_ukloniti:
        red = random.randint(0, 8)
        kolona = random.randint(0, 8)
        if tabla[red][kolona] != 0:
            tabla[red][kolona] = 0
            uklonjeno += 1

def prikazi_tablu(tabla):
    print("\n   Sudoku\n")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(tabla[i][j] if tabla[i][j] != 0 else ".", end=" ")
        print()
    print()

def sudoku_igra():
    tabla = prazna_tabla()
    popuni_tabelu(tabla)

    # Fiksiraj da na prvom mestu u prvom redu bude 4 (po želji)
    tabla[0][0] = 4

    resenje = [red[:] for red in tabla]
    ukloni_polja(tabla, 36)
    originalna_tabla = [red[:] for red in tabla]  # Čuvamo koja su polja fiksna

    while True:
        prikazi_tablu(tabla)
        unos = input("Unesi red, kolonu i broj (ili 0 za brisanje), npr. '1 2 5', ili 'q' za izlaz: ")
        if unos.lower() == 'q':
            print("Kraj igre.")
            break
        try:
            red, kolona, broj = map(int, unos.split())
            red -= 1
            kolona -= 1

            if not (0 <= red < 9 and 0 <= kolona < 9 and 0 <= broj <= 9):
                print("Unos mora biti u opsegu: red 1-9, kolona 1-9, broj 0-9.")
                continue

            if broj == 0:
                # Brisanje unosa, samo ako polje nije fiksno
                if originalna_tabla[red][kolona] == 0:
                    tabla[red][kolona] = 0
                    print(f"Obrisano polje na poziciji ({red+1}, {kolona+1}).")
                else:
                    print("To polje nije moguće obrisati jer je deo početne table.")
            else:
                # Unos broja
                if tabla[red][kolona] == 0:
                    if legalan_broj(tabla, broj, red, kolona):
                        tabla[red][kolona] = broj
                        if tabla == resenje:
                            prikazi_tablu(tabla)
                            print("Čestitamo! Rešili ste Sudoku!")
                            break
                    else:
                        print("Nelegalan potez. Taj broj ne može na tu poziciju.")
                else:
                    print("To polje nije prazno.")
        except ValueError:
            print("Unos mora biti u formatu: red kolona broj (npr. 3 4 5)")

if __name__ == "__main__":
    sudoku_igra()