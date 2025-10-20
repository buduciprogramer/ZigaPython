import numpy as np

n=20
mean1=20
std1=3

mean2=40
std2=5

# Generisanje dva niza iz normalne raspodjele
np.random.seed(0)
niz1 = np.random.normal(loc=mean1, scale=std1, size=n)
niz2 = np.random.normal(loc=mean2, scale=std2, size=n)

# Sabiranje nizova
niz_suma=niz1+niz2

# Izračunavanje srednje vrijednosti rezultujućeg niza
srednja_vrijednost = np.mean(niz_suma)

# Ispis
print("Niz 1:", np.round(niz1, 2))
print("Niz 2:", np.round(niz2, 2))
print("Zbirni niz:", np.round(niz_suma, 2))
print("Srednja vrijednost zbirnog niza:", round(srednja_vrijednost, 2))