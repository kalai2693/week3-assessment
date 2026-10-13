import pandas as pd

df = pd.read_csv("tickets_raw.csv")
before = len(df)

print("=== BEFORE CLEANING ===")
print("Rows:", before)
print("% missing:")
print((df.isna().mean() * 100).round(1))
print("Duplicates:", df.duplicated().sum())
print("Category counts:")
print(df["category"].value_counts())

# Fix casing first
df["text"] = df["text"].str.strip().str.lower()
df["category"] = df["category"].str.strip().str.title()

# Remove missing rows and duplicates
df = df.dropna()
df = df.drop_duplicates()

print()
print("=== AFTER CLEANING ===")
print(f"Rows {before} -> {len(df)} after cleaning")
print("Missing:", df.isna().sum().sum())
print("Duplicates:", df.duplicated().sum())
print("Category counts:")
print(df["category"].value_counts())

df.to_csv("tickets_clean.csv", index=False)