import pandas as pd

df = pd.read_csv("data/rice_dataset.csv")

print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nYear coverage:")
print(df["year"].min(), "-", df["year"].max())

print("\nTarget summary:")
print(df["yield_kg_per_ha"].describe())