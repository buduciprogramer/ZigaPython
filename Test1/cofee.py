import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Učitaj Excel fajl
df = pd.read_excel(r'C:\Users\PC\Desktop\coffe.xlsx', engine='openpyxl')

# Normalizuj nazive kolona (ukloni razmake, pretvori u mala slova)
df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
print("Kolone u datasetu:", df.columns.tolist())

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

# 7. Dodaj kolonu procentualne promjene cijene (ako postoji price)
if 'price' in df.columns:
    df['price_pct_change'] = df['price'].pct_change()

# 8. Dodaj kolonu ukupne vrijednosti transakcije (ako postoje price i quantity)
if 'price' in df.columns and 'quantity' in df.columns:
    df['total_value'] = df['price'] * df['quantity']

# 9. Dodaj kolonu ukupnog prihoda po vrsti kafe (koristi 'money')
total_per_coffee = None
if 'coffee_name' in df.columns and 'money' in df.columns:
    total_per_coffee = df.groupby('coffee_name')['money'].sum().reset_index()
    total_per_coffee.rename(columns={'money': 'total_revenue'}, inplace=True)
    df = pd.merge(df, total_per_coffee, on='coffee_name', how='left')

# 10. Sačuvaj očišćeni dataset kao coffee_analysis.csv
df.to_csv('coffee_analysis.csv', index=False)
print("\nSačuvan kao 'coffee_analysis.csv'")

# ------------------------------------------------------
# 11. VIZUALIZACIJE
# ------------------------------------------------------

sns.set(style="whitegrid")

# Kreiraj veću coffee-paletu (10 boja da ne bude cycling problema)
coffee_palette = sns.color_palette("Set3", n_colors=10)

# 1. Ukupan prihod po vrsti kafe
if total_per_coffee is not None:
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x='coffee_name',
        y='total_revenue',
        data=total_per_coffee,
        palette=coffee_palette
    )
    plt.title('Ukupan prihod po vrsti kafe')
    plt.xlabel('Vrsta kafe')
    plt.ylabel('Ukupan prihod (money)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("Nema dovoljno podataka za grafikon prihoda po vrsti kafe (provjeri kolone).")

# 2. Pie chart — udio prihoda po vrsti kafe
if total_per_coffee is not None:
    plt.figure(figsize=(8, 8))
    plt.pie(
        total_per_coffee['total_revenue'],
        labels=total_per_coffee['coffee_name'],
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("BrBG", len(total_per_coffee))
    )
    plt.title('Udio prihoda po vrsti kafe', fontsize=14)
    plt.tight_layout()
    plt.show()

# 3. Cijena kroz vrijeme (ako postoji kolona "date")
if 'date' in df.columns and 'price' in df.columns:
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='price', data=df, marker='o', color='#6D4C41')
    plt.title('Promjena cijene kroz vrijeme')
    plt.xlabel('Datum')
    plt.ylabel('Cijena')
    plt.tight_layout()
    plt.show()

# 4. Distribucija količina prodaje
if 'quantity' in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df['quantity'], bins=20, kde=True, color='#8B4513')
    plt.title('Distribucija količina prodaje')
    plt.xlabel('Količina')
    plt.ylabel('Frekvencija')
    plt.tight_layout()
    plt.show()

# 5. Ukupan prihod po danima u sedmici (ako ima weekday)
if 'weekday' in df.columns and 'money' in df.columns:
    plt.figure(figsize=(10, 6))
    # bez hue da nema cycling, koristimo samo paletu
    sns.barplot(x='weekday', y='money', data=df, estimator=sum, errorbar=None, palette=coffee_palette)
    plt.title('Ukupan prihod po danima u sedmici')
    plt.xlabel('Dan u sedmici')
    plt.ylabel('Ukupan prihod')
    plt.tight_layout()
    plt.show()

# 6. Ukupan prihod po mesecima (ako ima month_name)
if 'month_name' in df.columns and 'money' in df.columns:
    plt.figure(figsize=(10, 6))
    month_palette = sns.color_palette("tab20", 12)  # 12 boja za 12 meseci
    sns.barplot(x='month_name', y='money', data=df, estimator=sum, errorbar=None, palette=month_palette)
    plt.title('Ukupan prihod po mesecima')
    plt.xlabel('Mesec')
    plt.ylabel('Ukupan prihod')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#  7. Violin plot — distribucija prihoda po periodu dana
if 'time_of_day' in df.columns and 'money' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='time_of_day', y='money', data=df)
    plt.title('Distribucija prihoda po periodu dana')
    plt.xlabel('Dio dana')
    plt.ylabel('Prihod')
    plt.tight_layout()
    plt.show()

#  8. Heatmap — prihod po satu i danu (ako postoje hour_of_day i weekday)
if 'hour_of_day' in df.columns and 'weekday' in df.columns and 'money' in df.columns:
    heatmap_data = df.pivot_table(values='money', index='weekday', columns='hour_of_day', aggfunc='sum')
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap='YlOrBr', annot=True, fmt='.0f')
    plt.title('Prihod po satu i danu u sedmici')
    plt.xlabel('Sat u danu')
    plt.ylabel('Dan u sedmici')
    plt.tight_layout()
    plt.show()