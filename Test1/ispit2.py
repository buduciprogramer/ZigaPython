import pandas as pd

# Kreiranje DataFrame-a
sales_data = pd.DataFrame({
    'Proizvod': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Prodaja': [100, 150, 120, 200, 90, 180],
    'Količina': [10, 5, 8, 12, 9, 15]
})

# Grupisanje po 'Proizvod' i agregacija
rezultat = sales_data.groupby('Proizvod').agg({
    'Prodaja': 'sum',     # Ukupna prodaja
    'Količina': 'max'     # Maksimalna količina prodata
}).reset_index()

# Prikaz rezultata
print(rezultat)