import pandas as pd
import numpy as np

# Load dataset
anime_df = pd.read_csv("anime.csv")

### --------------------- UNIT I: NUMPY ---------------------

# Fixed type array
ratings = anime_df['rating'].dropna().astype(np.float32).values

# Creating arrays
arr = np.array([10, 20, 30, 40, 50])

# Array Indexing and Slicing
print("Indexing:", ratings[0], ratings[10])
print("Slicing:", ratings[5:10])

# Reshape array
reshaped = ratings[:12].reshape(3, 4)
print("Reshaped:\n", reshaped)

# Concatenate & Split
concat = np.concatenate([ratings[:3], ratings[3:6]])
split = np.split(ratings[:6], 2)
print("Concatenated:", concat)
print("Split:", split)

# Universal functions
print("Square Root:", np.sqrt(ratings[:5]))
print("Exponential:", np.exp(ratings[:5]))

# Aggregations
print("Mean:", np.mean(ratings))
print("Sum:", np.sum(ratings))

# Broadcasting
print("Broadcasting Add:", ratings[:5] + 1.5)

# Comparisons & Boolean Arrays
print("Ratings > 9:", ratings[ratings > 9])

# Fancy Indexing
print("Fancy Indexing:", ratings[[0, 3, 6]])

# Sorting
print("Sorted:", np.sort(ratings[:10]))
print("Argsort:", np.argsort(ratings[:10]))

# Structured Array
structured = np.array(
    [(row.anime_id, row.name, row.rating) for _, row in anime_df[['anime_id', 'name', 'rating']].dropna().head(5).iterrows()],
    dtype=[('anime_id', 'i4'), ('name', 'U50'), ('rating', 'f4')]
)
print("Structured Array:\n", structured)

### --------------------- UNIT II: PANDAS ---------------------

# Series & DataFrame
rating_series = pd.Series(anime_df['rating'])
anime_df_copy = anime_df.copy()

# Indexing
print("Series indexing:", rating_series[0:5])
print("DataFrame column:", anime_df['name'].head())

# Universal Functions
print("Square root of ratings:", np.sqrt(anime_df['rating'].dropna()).head())

# Index alignment
rating_plus_members = anime_df['rating'] + (anime_df['members'] / 1e6)

# Operations
mean_rating = anime_df['rating'].mean()
normalized_ratings = anime_df['rating'] - mean_rating

# Handling Missing Data
print("Missing values:\n", anime_df.isnull().sum())
filled_df = anime_df.fillna({'genre': 'Unknown', 'rating': mean_rating})
dropped_df = anime_df.dropna()

# Null values
print("Null genres:\n", anime_df[anime_df['genre'].isnull()])

# Hierarchical Indexing
multi_index_df = anime_df.set_index(['genre', 'type']).sort_index()

### --------------------- UNIT III: COMBINING DATASETS ---------------------

# Concatenation
top5 = anime_df.head(5)
bottom5 = anime_df.tail(5)
concat_df = pd.concat([top5, bottom5])

# Append (using concat because append is deprecated)
appended_df = pd.concat([top5, bottom5], ignore_index=True)

# Merge/Join
extra_df = pd.DataFrame({
    'anime_id': [32281, 5114],
    'studio': ['CoMix Wave', 'Bones']
})
merged_df = pd.merge(anime_df, extra_df, on='anime_id', how='left')

# Grouping
grouped = anime_df.groupby('type')['rating'].mean()
print("Grouped ratings by type:\n", grouped)

# Pivot Tables
anime_df['main_genre'] = anime_df['genre'].str.split(',').str[0]
pivot_cleaned = anime_df.pivot_table(values='rating', index='type', columns='main_genre', aggfunc='mean')
print("Pivot Table:\n", pivot_cleaned)
