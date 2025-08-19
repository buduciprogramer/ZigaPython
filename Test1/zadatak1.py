masa=float(input("Unesite masu u kilogramima (kg):"))
visina = float(input("Unesite visinu u metrima (m): "))

# Izračun BMI
bmi = masa / (visina ** 2)

# Određivanje statusa prema BMI
if bmi < 19.1:
    status = "prenizak"
elif 19.1 <= bmi <= 25.8:
    status = "idealan"
elif 25.9 <= bmi <= 27.3:
    status = "malo povišen"
elif 27.4 <= bmi <= 32.2:
    status = "visok"
elif 32.3 <= bmi <= 44.8:
    status = "previsok"
else:
    status = "izrazito visok"

# Ispis rezultata
print(f"\nVaš BMI iznosi: {bmi:.2f}")
print(f"Status: {status}")