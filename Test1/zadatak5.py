print("Dobrodošli u mini test ličnosti (MBTI verzija)!\n")
print("Odgovori na 4 pitanja unosom samo jednog slova po pitanju (npr. E, I, S, N, T, F, J, P).")
print("----------------------------------------------------------\n")

# Pitanje 1: E / I
print("1. Potpuno ste iscrpljeni jer ste imali beskrajno težak tjedan. Kako ćete provesti vikend?")
print("E - Zvat ću prijatelje i nešto organizovati.")
print("I - Ostaću kod kuće, gledati seriju, čitati, opustiti se sam/a.")
odg1 = input("Odgovor (E/I): ").strip().upper()

# Pitanje 2: S / N
print("\n2. Koji od ova dva opisa vam više odgovara?")
print("S - Fokusiram se na sadašnji trenutak i činjenice.")
print("N - Više volim sanjariti i oslanjam se na intuiciju.")
odg2 = input("Odgovor (S/N): ").strip().upper()

# Pitanje 3: T / F
print("\n3. Kako donosiš važne odluke?")
print("T - Logično i hladno, prikupljam sve podatke.")
print("F - Slušam svoje osjećaje i intuiciju.")
odg3 = input("Odgovor (T/F): ").strip().upper()

# Pitanje 4: J / P
print("\n4. Kako se pripremaš za važne događaje?")
print("J - Volim planirati unaprijed i biti spreman/na.")
print("P - Volim spontanost i uživam bez velikih priprema.")
odg4 = input("Odgovor (J/P): ").strip().upper()

# Kombinacija odgovora
tip = odg1 + odg2 + odg3 + odg4


tipovi = {
    "ESTJ": "Upravitelj",
    "ENTJ": "Narednik",
    "ESFJ": "Učitelj",
    "ESTP": "Maršal",
    "ENFJ": "Mentor",
    "ENTP": "Inovator",
    "ESFP": "Političar",
    "ENFP": "Pobjednik",
    "INFP": "Iscjelitelj",
    "ISFP": "Skladatelj"
}

# Rezultat
print("\n----------------------------------------------------------")
print(f"Vaš tip ličnosti je: {tip}")
if tip in tipovi:
    print(f"Opis: {tipovi[tip]}")
else:
    print("Ne postoji opis za ovu kombinaciju, ali si jedinstven/a!")