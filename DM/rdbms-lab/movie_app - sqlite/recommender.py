# recommender.py

import numpy as np
import pickle, os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarities(db):
    """
    Computes the similarity scores between movies based on text analysis of their descriptions, keywords, genres, 
    and cast information, and saves the resulting similarity matrix to a file named 'similarity.pkl'.

    Parameters:
    db (sqlite3.Connection): A database connection object used to execute SQL queries and fetch movie-related data.

    Returns:
    numpy.ndarray: A 2D array representing the cosine similarity matrix between movies, where each element (i, j) 
                   represents the similarity score between movie i and movie j.
    """

    # reading tables using pandas
    mv = pd.read_sql_query("SELECT * FROM movies", db)
    ge = pd.read_sql_query("SELECT * FROM genres", db)
    kw = pd.read_sql_query("SELECT * FROM keywords", db)
    # CORRECTED to use 'people' table
    pe = pd.read_sql_query("SELECT * FROM people", db)

    # collect all keywords for each movie in a list
    grouped_kw = kw\
        .assign(keyword = kw.keyword.str.replace(" ", "_").str.lower())\
        .groupby("movie_id")\
        .agg(keyword = ("keyword", lambda x: " ".join(list(x))))\
        .reset_index()

    # collect all people for each movie in a list
    grouped_pe = pe\
        .assign(name = pe.name.str.replace(" ", "_").str.lower())\
        .groupby("movie_id")\
        .agg(cast = ("name", lambda x: " ".join(list(x)[:3])))\
        .reset_index()

    # collect all genres for each movie in a list
    grouped_ge = ge\
        .assign(genre = ge.genre.str.replace(" ", "_").str.lower())\
        .groupby("movie_id")\
        .agg(genre = ("genre", lambda x: " ".join(list(x))))\
        .reset_index()

    # merge all dataframes
    merged_df = pd\
        .merge(mv, grouped_kw, how="left", left_on = "id", right_on="movie_id")\
        .merge(grouped_pe,  how="left", left_on = "id", right_on="movie_id")\
        .merge(grouped_ge,  how="left", left_on = "id", right_on="movie_id")

    # replace NaN values with an empty string
    merged_df = merged_df.where(pd.notna(merged_df), "")

    # concatenate plot, keywords, genres, and cast into one text to be vectorized
    merged_df["text"] = merged_df['overview'].str.lower() + " " + merged_df['keyword'] + " " + merged_df['genre'] + " " + merged_df['cast']
    
    # perform text vectorization 
    ps = PorterStemmer()
    
    def normalize_text(text):
        stems = []
        for i in text.split():
            stems.append(ps.stem(i))
            
        return " ".join(stems)
        
    # normalize each text using Porter Stemmer
    normalized_text = merged_df['text'].apply(normalize_text)

    # transform a text into a vector based on the frequency (count) of each word in the whole corpus.
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(normalized_text).toarray()

    # Cosine similarity is often used to measure document similarity in text analysis.
    similarity = cosine_similarity(vectors)
    pickle.dump(similarity, open('similarity.pkl', 'wb'))
    return similarity



def recommend(db, movie_id, n=3):
    """
    Recommends a specified number of movies that are similar to a given movie based on precomputed similarity scores.

    Parameters:
    db (sqlite3.Connection): A database connection object used to execute SQL queries and fetch movie data.
    movie_id (int): The ID of the movie for which recommendations are to be generated.
    n (int, optional): The number of similar movies to recommend. Default is 3.

    Returns:
    list of int: List of IDs of the recommended movies.
    """

    # check if the similarities are already computed.
    if "similarity.pkl" not in os.listdir():
        similarities = compute_similarities(db)
    else:
        similarities = pickle.load(open('similarity.pkl', 'rb'))
    
    # Read the whole movie table and find the index of the movie
    movies_df = pd.read_sql_query("SELECT id FROM movies", db)
    
    if movie_id not in movies_df['id'].values:
        return [] # Return an empty list if the movie_id is not found
        
    movie_index = movies_df[movies_df['id'] == movie_id].index[0]

    # Get the similarity scores with other movies
    distances = similarities[movie_index]

    # Sort the similarity scores to find the top 'n' most similar movies, excluding the given movie itself.
    movie_ids = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:1+n]
    recommended_ids = []

    # Retrieve the IDs and titles of the recommended movies.
    for (index, similarity_value) in movie_ids:
        movie_id_val = movies_df.iloc[index].id
        recommended_ids.append(int(movie_id_val))
    return recommended_ids