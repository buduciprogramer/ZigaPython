import numpy as np

niz=np.array([5,10,15,20,
              25,35,45,55,
              65,75,85,90])

print("Originalni niz:")
print(niz)
print("Dimenzije originalnog niza:", niz.shape)

# Promjena oblika niza u (2, 6)
niz_reshaped = niz.reshape(2, 6)
print("\nNiz nakon reshape u (2, 6):")
print(niz_reshaped)

# Matematičke operacije
suma = np.sum(niz_reshaped)
prosjek = np.mean(niz_reshaped)
minimum = np.min(niz_reshaped)
maksimum = np.max(niz_reshaped)

print("\nMatematičke operacije:")
print(f"Suma elemenata: {suma}")
print(f"Aritmetička sredina: {prosjek}")
print(f"Minimalna vrijednost: {minimum}")
print(f"Maksimalna vrijednost: {maksimum}")