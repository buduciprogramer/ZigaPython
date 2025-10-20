import pandas as pd

# Učitajte CSV fajl
df = pd.read_csv('movies')

# Pretpostavljam da je naziv kolone 'Audience score %'
# Ako je drugačije, proverite naziv kolone u CSV fajlu i prilagodite

# Filtrirajte podatke gde je Audience score % između 20 i 80
filtered_df = df[(df['Audience score %'] >= 20) & (df['Audience score %'] <= 80)]

# Sačuvajte filtrirane podatke u novi CSV
filtered_df.to_csv('filtered_movies.csv', index=False)

print("Filtrovanje završeno. Podaci sačuvani u 'filtered_movies'.")