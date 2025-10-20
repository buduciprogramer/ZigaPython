import pandas as pd

df=pd.read_csv("academic_stress")

# 2. Obradi NaN vrijednosti
df['stress_level'] = df['stress_level'].fillna(df['stress_level'].mean())
df['study_hours'] = df['study_hours'].fillna(df['study_hours'].median())

# 3. Konvertuj tipove
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 4. Kreiraj nove kolone
df['total_hours'] = df['study_hours'] + df['sleep_hours']
df['stress_change_pct'] = df.groupby('student_id')['stress_level'].pct_change()

# 5. Spasi očišćeni dataset
df.to_csv("cleaned_data.csv", index=False)