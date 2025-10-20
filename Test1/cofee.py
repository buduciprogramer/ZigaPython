import pandas as pd

# 1. Učitaj Excel fajl
df = pd.read_excel(r'C:\Users\PC\Desktop\coffe.xlsx', engine='openpyxl')
print(df.head())


# 2. Prikaz prvih 5 redova
print("Prvih 5 redova:")
print(df.head())

# 3. Provjera nedostajućih vrijednosti
print("\nNedostajuće vrijednosti po kolonama:")
print(df.isnull().sum())

# 4. Uklanjanje redova sa nedostajućim podacima
df = df.dropna()

# 5. Provjera i konverzija tipova podataka
print("\nTipovi podataka:")
print(df.dtypes)

if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'])

# 6. Sortiraj po datumu ako postoji
if 'date' in df.columns:
    df = df.sort_values('date')

# 7. Dodaj kolonu procentualne promjene cijene
if 'price' in df.columns:
    df['price_pct_change'] = df['price'].pct_change()

# 8. Dodaj kolonu ukupne vrijednosti transakcije
if 'price' in df.columns and 'quantity' in df.columns:
    df['total_value'] = df['price'] * df['quantity']

# 9. Dodaj kolonu ukupnog prihoda po vrsti kafe
if 'coffee_name' in df.columns and 'total_value' in df.columns:
    total_per_coffee = df.groupby('coffee_name')['total_value'].sum().reset_index()
    total_per_coffee.rename(columns={'total_value': 'total_revenue'}, inplace=True)
    df = pd.merge(df, total_per_coffee, on='coffee_name', how='left')

# 10. Sačuvaj očišćeni dataset kao coffee_analysis.csv
df.to_csv('coffee_analysis.csv', index=False)
print("\nSačuvan kao 'coffee_analysis.csv'")