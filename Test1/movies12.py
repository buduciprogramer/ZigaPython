import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
#  Učitaj dataset i pripremi ga
file_path = r"C:\Users\PC\Desktop\movies12.csv"  # promijeni putanju ako je drugačija
df = pd.read_csv(file_path)

# Preimenuj kolone radi lakše upotrebe
df = df.rename(columns={
    'Genre': 'genre',
    'Lead Studio': 'lead_studio',
    'Audience score %': 'audience_score',
    'Profitability': 'profitability',
    'Rotten Tomatoes %': 'rotten_tomatoes_score',
    'Year': 'release_year'
})

# Pretvori numeričke kolone u brojeve
for col in ['audience_score', 'profitability', 'rotten_tomatoes_score', 'release_year']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Ako je genre string sa zarezima, pretvori u listu
df['genre'] = df['genre'].str.split(', ')

# -----------------------------
# 2️⃣ Histogram distribucije ocjena filmova (audience_score)
plt.figure(figsize=(10, 6))
plt.hist(df['audience_score'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Distribucija ocjena filmova (Audience Score)')
plt.xlabel('Audience Score')
plt.ylabel('Broj filmova')
plt.grid(True)
plt.show()

# -----------------------------
# 3️⃣ Bar chart: prosječni audience_score po žanrovima
df_genres = df.explode('genre')  # svaki žanr u svom redu
avg_audience_score = df_genres.groupby('genre')['audience_score'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
avg_audience_score.plot(kind='bar', color='lightcoral')
plt.title('Prosječni Audience Score po žanrovima')
plt.xlabel('Žanr')
plt.ylabel('Prosječni Audience Score')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

# -----------------------------
#  Povezanost između profitability i Rotten Tomatoes ocjene
correlation = df[['profitability', 'rotten_tomatoes_score']].corr().iloc[0, 1]
print(f'Korelacija između profitability i Rotten Tomatoes ocjene: {correlation:.2f}')

plt.figure(figsize=(10, 6))
plt.scatter(df['profitability'], df['rotten_tomatoes_score'], alpha=0.5, color='green')
plt.title('Povezanost između Profitability i Rotten Tomatoes ocjene')
plt.xlabel('Profitabilnost')
plt.ylabel('Rotten Tomatoes ocjena')
plt.grid(True)
plt.show()

# -----------------------------
#  Prosječna profitabilnost po vodećim studijima
avg_profitability_by_studio = df.groupby('lead_studio')['profitability'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 8))
avg_profitability_by_studio.plot(kind='bar', color='lightgreen')
plt.title('Prosječna Profitabilnost po vodećim studijima')
plt.xlabel('Vodeći studio')
plt.ylabel('Prosječna profitabilnost')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

# -----------------------------
# 6️⃣ Evolucija prosječne Rotten Tomatoes ocjene kroz godine
avg_rt_by_year = df.groupby('release_year')['rotten_tomatoes_score'].mean()

plt.figure(figsize=(10, 6))
avg_rt_by_year.plot(kind='line', marker='o', color='blue')
plt.title('Evolucija prosječne Rotten Tomatoes ocjene kroz godine')
plt.xlabel('Godina')
plt.ylabel('Prosječna Rotten Tomatoes ocjena')
plt.grid(True)
plt.show()