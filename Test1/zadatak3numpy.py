import numpy as np

cijene=np.array([100, 102, 107, 106, 112, 110, 120, 119, 125, 132])

# Pretpostavljene dnevne cijene dionice
promjene=np.diff(cijene)/cijene[:-1] *100

# Izračunaj postotne promjene u odnosu na prethodni dan
# (npr. (danas - jučer) / jučer) * 100

promjene=np.diff(cijene)/cijene[:-1] *100


# Pronađi indekse gdje je promjena veća od 5%
indeksi_skoka = np.where(promjene > 5)[0] + 1  # +1 jer diff smanjuje dužinu za 1

# Ispis rezultata
print("Promjene u % po danima:", promjene)
print("Indeksi dana kada je došlo do skoka > 5%:", indeksi_skoka)
print("Cijene na te dane:", cijene[indeksi_skoka])

