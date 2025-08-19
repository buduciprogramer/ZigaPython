broj_dionica=int(input("Koliko dionica želite da unesete"))

dionice={}
for _ in range(broj_dionica):
    oznaka = input("Unesite oznaku dionice (npr. AAPL): ").upper()
    cijene_str = input(f"Unesite cijene za {oznaka} (razdvojene razmakom): ")
    cijene = list(map(float, cijene_str.split()))
    dionice[oznaka] = cijene

print("\n--- Prosječne cijene ---")
prosjecne_cijene = {}
for oznaka, cijene in dionice.items():
    prosjek = sum(cijene) / len(cijene)
    prosjecne_cijene[oznaka] = prosjek
    print(f"{oznaka}: {prosjek:.2f}")

print("\n--- Dionica sa najvećim rastom ---")
najveca_razlika = None
oznaka_najveci_rast = ""
for oznaka, cijene in dionice.items():
    rast = cijene[-1] - cijene[0]
    if najveca_razlika is None or rast > najveca_razlika:
        najveca_razlika = rast
        oznaka_najveci_rast = oznaka

print(f"{oznaka_najveci_rast} (rast: {najveca_razlika:.2f})")

print("\n--- Ukupna vrijednost portfolija (10 dionica svake vrste) ---")
ukupna_vrijednost = 0
for oznaka, cijene in dionice.items():
    vrijednost = cijene[-1] * 10
    ukupna_vrijednost += vrijednost
print(f"Ukupna vrijednost: {ukupna_vrijednost:.2f}")

print("\n--- Dionice sortirane po prosječnoj cijeni (od najveće ka najmanjoj) ---")
sortirane = sorted(prosjecne_cijene.items(), key=lambda x: x[1], reverse=True)
for oznaka, prosjek in sortirane:
    print(f"{oznaka}: {prosjek:.2f}")