# movie_app.py

import streamlit as st
import sqlite3
import pandas as pd
from recommender import recommend
import os

# --- Robust Path Configuration ---
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "tmdb", "movies_and_recommendations.db")
image_path = os.path.join(script_dir, "deadpool.png")


# --- Database Connection ---
if not os.path.exists(db_path):
    st.error(f"Database file not found. Expected at: {db_path}")
    st.stop()

db = sqlite3.connect(db_path)
cursor = db.cursor()


# --- App Layout ---
if os.path.exists(image_path):
    st.image(image_path)
else:
    st.warning("deadpool.png not found, skipping header image.")

st.title("Welcome to the Movie App! :movie_camera:")
st.markdown("Discover your next movie adventure.")


# --- Genre Selection ---
sql_genres = """
SELECT genre, count(movie_id) AS n_movies
    FROM genres
    GROUP BY genre
    ORDER BY 2 DESC
"""
genres = pd.read_sql_query(sql_genres, db)
selected_genre = st.selectbox(label="What is your vibe today?", options=genres["genre"])


# --- Movie Selection ---
sql_movies_in_genre = """
    SELECT title, popularity, vote_average
    FROM movies INNER JOIN genres ON movies.id = genres.movie_id
    WHERE genre = ?
    ORDER BY popularity DESC
    LIMIT 10
"""
movies_in_genre = pd.read_sql_query(sql_movies_in_genre, db, params=(selected_genre,))
st.table(movies_in_genre)


# --- Movie Info Display ---
selected_title = st.selectbox(label="Pick a title", options=movies_in_genre["title"])

if selected_title:
    sql_movie_info = """
        SELECT id, title, tagline, overview, image_url
        FROM movies
        WHERE title = ?
    """
    cursor.execute(sql_movie_info, (selected_title,))
    movie_info = cursor.fetchone()
    
    if movie_info:
        movie_id, _, movie_tagline, movie_overview, image_url = movie_info

        poster_col, info_col = st.columns([0.3, 0.7])

        if image_url:
            poster_col.image(image_url)
        info_col.markdown(f"**{selected_title}**")
        info_col.markdown(f"*{movie_tagline}*")
        info_col.markdown(movie_overview)

        # --- Cast Display ---
        st.markdown("---")
        st.markdown("**Top Billed Cast**")
        # CORRECTED to use 'people' table
        sql_movie_cast = """
            SELECT person_id, name, character, image_url
            FROM people
            WHERE movie_id = ?
            LIMIT 5
        """
        cursor.execute(sql_movie_cast, (movie_id,))
        movie_cast = cursor.fetchall()

        if movie_cast:
            cols = st.columns(len(movie_cast))
            for i, col in enumerate(cols):
                person_id, name, character, cast_image_url = movie_cast[i]
                if cast_image_url:
                    col.image(cast_image_url, caption=name)
                else:
                    col.caption(name)
                col.markdown(f"*{character}*")

        # --- Recommendation Section ---
        st.markdown("---")
        if st.button("Recommend movies!"):
            n_movies_to_recommend = 3
            recommended_ids = recommend(db, movie_id, n=n_movies_to_recommend)

            if recommended_ids:
                st.markdown(f"If you liked *{selected_title}*, check out these:")
                rec_cols = st.columns(n_movies_to_recommend)
                for i, col in enumerate(rec_cols):
                    sql_similar_movie = """
                        SELECT title, image_url
                        FROM movies
                        WHERE id = ?
                    """
                    similar_movie_id = recommended_ids[i]
                    title, poster = cursor.execute(sql_similar_movie, (similar_movie_id,)).fetchone()
                    if poster:
                        col.image(poster, caption=title)
                    else:
                        col.caption(title)
            else:
                st.warning("Could not generate recommendations for this movie.")

# Close the database connection
db.close()