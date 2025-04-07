import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Set seaborn style
sns.set(style="whitegrid")

# Load the cleaned dataset
df = pd.read_csv("netflix_cleaned.csv")

# --- 1. Distribution of Movies vs TV Shows ---
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='type', hue='type', palette='Set2', legend=False)
plt.title("Distribution of Movies and TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("distribution_movies_tvshows.png")  # Save instead of show
# plt.show()

# --- 2. Top 10 Countries by Content Count ---
plt.figure(figsize=(10, 5))
df['country'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 Countries by Content")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_10_countries.png")
# plt.show()

# --- 3. Content Added Per Year ---
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='year_added', order=sorted(df['year_added'].dropna().unique()), palette='Set3')
plt.title("Content Added Per Year")
plt.xticks(rotation=45)
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_added_per_year.png")
# plt.show()

# --- 4. Top 10 Most Common Genres ---
genres = df['listed_in'].str.split(', ').sum()
genre_counts = Counter(genres).most_common(10)
top_genres = pd.DataFrame(genre_counts, columns=['Genre', 'Count'])

plt.figure(figsize=(10, 6))
sns.barplot(data=top_genres, y='Genre', x='Count', hue='Genre', palette='mako', legend=False)
plt.title("Top 10 Most Common Genres")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.tight_layout()
plt.savefig("top_10_genres.png")
# plt.show()

# --- 5. Duration Split: Minutes vs Seasons ---
df['duration_type'] = df['duration'].apply(lambda x: 'Season(s)' if 'Season' in str(x) else 'Minute(s)')

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='duration_type', hue='duration_type', palette='pastel', legend=False)
plt.title("Content Duration Type")
plt.xlabel("Duration Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("duration_type.png")
# plt.show()