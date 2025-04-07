import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")
print("Original Shape:", df.shape)

# Check missing values
print("\nMissing values:\n", df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values (safe method to avoid chained assignment warning)
df.loc[:, 'director'] = df['director'].fillna('Unknown')
df.loc[:, 'cast'] = df['cast'].fillna('Unknown')
df.loc[:, 'country'] = df['country'].fillna('Unknown')
df.loc[:, 'rating'] = df['rating'].fillna('Not Rated')
df.loc[:, 'duration'] = df['duration'].fillna('Unknown')

# Convert 'date_added' to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df.loc[:, 'date_added'] = df['date_added'].fillna(pd.Timestamp("2000-01-01"))  # fallback date

# Drop rows with critical missing values (if any remain)
df = df.dropna(subset=['title', 'type'])

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Clean text-based columns
df['country'] = df['country'].str.strip().str.title()
df['rating'] = df['rating'].str.strip().str.upper()
df['type'] = df['type'].str.strip().str.capitalize()

# Final check
print("\nCleaned Shape:", df.shape)
print("\nRemaining Missing Values:\n", df.isnull().sum())

# Save cleaned dataset
df.to_csv("netflix_cleaned.csv", index=False)
