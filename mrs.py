import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv(r"C:\Users\My PC\OneDrive\Documents\VsCode\MyWorkspace\Movies.csv")
print(df.head())


# Combine features (genre + description)
df['features'] = df['Genre'] + df['Description']

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['features'])

# Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies
def recommend_movie(title, num_recommendations=6):
    if title not in df['Title'].values:
        return f"Movie '{title}' not found in database!"
    
    idx = df.index[df['Title'] == title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    
    movie_indices = [i[0] for i in sim_scores]
    return df['Title'].iloc[movie_indices]

# Test the system
print("Recommendations for 'The Matrix':")
print(recommend_movie("The Matrix"))

print("Recommendations for 'Inception':")
print(recommend_movie("Inception"))

print("Recommendations for 'Toy Story':")
print(recommend_movie("Toy Story"))

print("Recommendations for 'The Godfather':")
print(recommend_movie("The Godfather"))

print("Recommendations for 'The Dark Knight':")
print(recommend_movie("The Dark Knight"))

print("Recommendations for 'Finding Nemo':")
print(recommend_movie("Finding Nemo"))

print("Recommendations for 'Interstellar':")
print(recommend_movie("Interstellar"))

print("Recommendations for 'Avengers':")
print(recommend_movie("Avengers"))