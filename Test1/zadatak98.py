import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\PC\Desktop\sol_data.csv"
df = pd.read_csv(file_path)

# Izgled prvih redaka da znamo sto imamo
print(df.head())

# Kreiraj kolonu 'tip' za lakšu čitljivost
df['tip'] = df['isPlanet'].apply(lambda x: 'Planet' if x else 'Ne-planet')

# Izračun prosječne mase (u 10^24 kg radi lakše usporedbe)
df['masa_10e24'] = df['mass_kg'] / 1e24

masa_po_tipu = df.groupby('tip')['masa_10e24'].mean().reset_index()

# Korelacija mase i udaljenosti od sunca (semimajorAxis u km)
planeti = df[df['isPlanet'] == True]
korelacija = planeti['semimajorAxis'].corr(planeti['masa_10e24'])

# Boxplot za gustoću planeta vs ne-planeta
plt.figure(figsize=(10, 6))
sns.boxplot(x='tip', y='density', data=df)
plt.title('Usporedba gustoće: Planeti vs Ne-planeti')
plt.xlabel('')
plt.ylabel('Gustoća (g/cm³)')
plt.show()

# Bar chart prosječne mase po tipu
plt.figure(figsize=(8, 6))
sns.barplot(x='tip', y='masa_10e24', data=masa_po_tipu)
plt.title('Prosječna masa po tipu tijela (10^24 kg)')
plt.ylabel('Masa (10^24 kg)')
plt.xlabel('')
plt.show()

print("\nProsječna masa po tipu tijela:")
print(masa_po_tipu)

print(f"\nKorelacija između udaljenosti od Sunca i mase planeta: {korelacija:.3f}")