import numpy as np

imena_voca = np.array(['jabuka', 'banana', 'naranca', 'kruska', 'mango'])
tezina_voca = np.array([150, 120, 180, 90, 200])

sort_indeks_ime=np.argsort(imena_voca)
imena_sortirana=imena_voca[sort_indeks_ime]
tezine_sortirano_ime=tezina_voca[sort_indeks_ime]

print("Sortirano po imenu:")
for ime, tezina in zip(imena_sortirana, tezine_sortirano_ime):
    print(f"{ime}: {tezina}g")

sort_indeksi_tezina = np.argsort(tezina_voca)
tezine_sortirano = tezina_voca[sort_indeksi_tezina]
imena_sortirano_tezina = imena_voca[sort_indeksi_tezina]

print("\nSortirano po tezini:")
for ime, tezina in zip(imena_sortirano_tezina, tezine_sortirano):
    print(f"{ime}: {tezina}g")

# 3. Prosječna težina
prosjek = np.mean(tezina_voca)
print(f"\nProsječna težina voća: {prosjek:.2f}g")

# 4. Filtriranje voća čija je težina > 130g
masivno_voce_maska = tezina_voca > 130
masivno_voce_imena = imena_voca[masivno_voce_maska]
masivno_voce_tezine = tezina_voca[masivno_voce_maska]

print("\nVoće teže od 130g:")
for ime, tezina in zip(masivno_voce_imena, masivno_voce_tezine):
    print(f"{ime}: {tezina}g")

