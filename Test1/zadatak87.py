import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

# Putanja do fajla
file_path = r"C:\Users\PC\Desktop\Sleep_health_and_lifestyle_dataset.csv"

# Učitavanje podataka
df = pd.read_csv(file_path)

# Parsiranje sistoličkog i dijastoličkog pritiska iz kolone 'Blood Pressure'
df[['sistolicki', 'dijastolicki']] = df['Blood Pressure'].str.split('/', expand=True).astype(int)

# Sačuvaj novi fajl (nije obavezno za crtanje, ali možeš za Tableau)
df.to_csv(r"C:\Users\PC\Desktop\Sleep_health_processed.csv", index=False)

# Scatter plot: dob vs sistolički pritisak, boje za muškarce i žene
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='sistolicki', hue='Gender', palette={'Male': 'blue', 'Female': 'red'})
plt.title('Odnos između dobi i sistoličkog pritiska')
plt.xlabel('Dob')
plt.ylabel('Sistolički pritisak')
plt.grid(True)
plt.show()

# Boxplot: dijastolički pritisak prema spolu
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='Gender', y='dijastolicki', palette={'Male': 'lightblue', 'Female': 'lightpink'})
plt.title('Dijastolički pritisak prema spolu')
plt.xlabel('Spol')
plt.ylabel('Dijastolički pritisak')
plt.grid(True)
plt.show()

# Statistike za sistolički pritisak
mean_sys = df['sistolicki'].mean()
median_sys = df['sistolicki'].median()
std_sys = df['sistolicki'].std()

print(f"Srednja vrijednost sistoličkog pritiska: {mean_sys:.2f}")
print(f"Medijan sistoličkog pritiska: {median_sys}")
print(f"Standardna devijacija sistoličkog pritiska: {std_sys:.2f}")

# Korelacija između dobi i sistoličkog pritiska
correlation = df['Age'].corr(df['sistolicki'])
print(f"Korelacija između dobi i sistoličkog pritiska: {correlation:.2f}")