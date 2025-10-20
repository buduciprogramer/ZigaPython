import pandas as pd
import numpy as np

# Inicijalni podaci
data = {
    'ID_studenta': [1, 2, 3, 1, 2, 3],
    'Predmet': ['Matematika', 'Matematika', 'Matematika', 'Engleski', 'Engleski', 'Engleski'],
    'Ocjena': [90, np.nan, 85, 75, 80, np.nan]
}

df = pd.DataFrame(data)

# 1. Popuni NaN ocjene srednjom ocjenom po predmetu
df['Ocjena'] = df.groupby('Predmet')['Ocjena'].transform(lambda x: x.fillna(x.mean()))

# 2. Ukloni duplikate (isti student, isti predmet)
df = df.drop_duplicates(subset=['ID_studenta', 'Predmet'])

# 3. Izračunaj prosječnu ocjenu po studentu
prosjeci = df.groupby('ID_studenta')['Ocjena'].mean().reset_index()
prosjeci.columns = ['ID_studenta', 'Prosjecna_ocjena']

# Prikaz rezultata
print(" Finalni DataFrame bez duplikata i NaN vrijednosti:")
print(df)

print("\n Prosječna ocjena po studentu:")
print(prosjeci)
