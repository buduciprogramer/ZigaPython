import pandas as pd

# Podaci
employee_data = pd.DataFrame({
    'ID_zaposlenika': [101, 102, 103, 104, 105],
    'Ime': ['muhamed', 'Bob', 'Čarli', 'David', 'sara'],
    'Plaća': [60000, 75000, 80000, 70000, 90000]
})

# 1. Izračun prosječne plaće
prosjecna_placa = employee_data['Plaća'].mean()
print(f"Prosječna plaća: {prosjecna_placa}")

# 2. Odabir zaposlenika s većom plaćom od prosječne
iznad_prosjeka = employee_data[employee_data['Plaća']>prosjecna_placa]
print("\nZaposlenici s plaćom iznad prosjeka:")
print(iznad_prosjeka)

# 3. Povećanje plaće za 10% za te zaposlenike
employee_data.loc[employee_data['Plaća']>prosjecna_placa,'Plaća'] *=1.10
print("\nAžurirani podaci nakon povećanja plaće za 10%:")
print(employee_data)