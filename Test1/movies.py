import pandas as pd

# Load the dataset
df = pd.read_csv("Test1\movies1.csv")

# Clean column names (optional)
df.columns = [col.strip().replace(" ", "_") for col in df.columns]

# Convert necessary columns to numeric (remove $ and commas)
df['Worldwide_Gross'] = df['Worldwide_Gross'].replace('[\$,]', '', regex=True).astype(float)
df['Profitability'] = pd.to_numeric(df['Profitability'], errors='coerce')
df['Audience_score_%'] = pd.to_numeric(df['Audience_score_%'], errors='coerce')
df['Rotten_Tomatoes_%'] = pd.to_numeric(df['Rotten_Tomatoes_%'], errors='coerce')

# Filter data: remove rows where Audience score % is < 20 or > 80
filtered_df = df[(df['Audience_score_%'] >= 20) & (df['Audience_score_%'] <= 80)]

# Compute correlations
correlations = filtered_df.corr(numeric_only=True)['Audience_score_%'].drop('Audience_score_%')

# Get positively and negatively correlated columns
positive_corr = correlations[correlations > 0].sort_values(ascending=False)
negative_corr = correlations[correlations < 0].sort_values()

print(" Positively correlated columns with Audience score %:")
print(positive_corr)

print("\n Negatively correlated columns with Audience score %:")
print(negative_corr)