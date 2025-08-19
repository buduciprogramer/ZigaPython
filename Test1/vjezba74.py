unos = input("Unesi temperature u Farenhajtima, odvojene zarezom: ")
farenhajti = [float(temp.strip()) for temp in unos.split(",")]
celzijusi = [round((f - 32) * 5 / 9, 2) for f in farenhajti]

print("Temperatura u Celzijusima:")
print(celzijusi)
