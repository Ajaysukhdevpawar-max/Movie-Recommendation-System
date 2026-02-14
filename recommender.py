import pandas as pd
import streamlit as st


df = pd.read_csv("movies.csv")

# Keep required columns
df = df[['title', 'overview', 'genres', 'vote_average']]

# Handle missing values
df['overview'] = df['overview'].fillna('')
df['genres'] = df['genres'].fillna('')

# Normalize genres
df['genres_lower'] = df['genres'].str.lower()


def recommend_by_genres(user_input, top_n=10):
    # Normalize input
    user_input = user_input.lower().replace('|', ',')
    selected_genres = [g.strip() for g in user_input.split(',') if g.strip()]

    if not selected_genres:
        print("❌ Please enter at least one genre.")
        return

    # Filter movies that contain ALL selected genres
    filtered_movies = df.copy()

    for genre in selected_genres:
        filtered_movies = filtered_movies[
            filtered_movies['genres_lower'].str.contains(genre)
        ]

    if filtered_movies.empty:
        print("❌ No movies found matching all selected genres.")
        return

    # Sort by rating
    filtered_movies = filtered_movies.sort_values(
        by='vote_average', ascending=False
    )

    print(f"\n🎬 Top {top_n} Movies / Web Series for genres: {', '.join(g.title() for g in selected_genres)}\n")

    for _, row in filtered_movies.head(top_n).iterrows():
        print(f"⭐ {row['title']} | Rating: {row['vote_average']}")


if __name__ == "__main__":
    print("🎥 AI Multi-Genre Movie & Web Series Recommendation System")
    print("--------------------------------------------------------")
    print("Enter one or more genres (Action, Sci-Fi, Drama etc.)")
    print("Type 'exit' to quit\n")

    while True:
        user_genres = input("Enter preferred genre(s): ")

        if user_genres.lower() == "exit":
            print("👋 Thank you for using the recommendation system!")
            break

        recommend_by_genres(user_genres)
        print("\n" + "-" * 50 + "\n")
