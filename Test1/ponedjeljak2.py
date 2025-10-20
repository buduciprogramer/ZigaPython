import numpy as np
import random

# Početni raspored prijatelja
prijatelji = np.array(["maja", "kenan", "kelvin", "newton", "farenhajt"])

# Pretvori u listu da bi random.shuffle radio kako treba
prijatelji_lista = prijatelji.tolist()

# Slučajno promiješaj
random.shuffle(prijatelji_lista)

# Vrati kao np.array ako ti treba dalje kao NumPy
prijatelji_pomiješani = np.array(prijatelji_lista)

# Ispis rezultata
print("Slučajno premještena mjesta:")
print(prijatelji_pomiješani)