
import pandas as pd
import numpy as np
import ast
import json

def load_data():
    movies = pd.read_csv('data/tmdb_5000_movies.csv')
    credits = pd.read_csv('data/tmdb_5000_credits.csv')
    return movies, credits

def preprocess_data(movies, credits):
    # Merge datasets
    df = pd.merge(movies, credits, left_on='id', right_on='movie_id', how='left')

    # Drop unnecessary columns
    df = df.drop(['homepage', 'id', 'keywords', 'original_language', 'overview', 'production_companies',
                  'production_countries', 'release_date', 'spoken_languages', 'status', 'tagline', 'title_y',
                  'movie_id', 'title_x', 'crew'], axis=1)

    # Handle missing values
    df['budget'] = df['budget'].fillna(df['budget'].median())
    df['revenue'] = df['revenue'].fillna(df['revenue'].median())
    df['runtime'] = df['runtime'].fillna(df['runtime'].median())
    df['popularity'] = df['popularity'].fillna(df['popularity'].median())
    df['vote_average'] = df['vote_average'].fillna(df['vote_average'].median())
    df['vote_count'] = df['vote_count'].fillna(df['vote_count'].median())

    # Parse genres
    df['genres'] = df['genres'].apply(lambda x: x.split(',') if pd.notnull(x) and x != '' else [])
    df['genre_count'] = df['genres'].apply(len)

    # Parse cast
    df['cast'] = df['cast'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)] if pd.notnull(x) else [])
    df['cast_size'] = df['cast'].apply(len)

    # Create target: Success based on revenue vs budget
    df['profit'] = df['revenue'] - df['budget']
    def categorize_success(row):
        if row['profit'] < 0:
            return 'Flop'
        elif row['profit'] < row['budget']:
            return 'Average'
        else:
            return 'Hit'
    df['success'] = df.apply(categorize_success, axis=1)

    # Select features
    features = ['budget', 'popularity', 'runtime', 'vote_average', 'vote_count', 'genre_count', 'cast_size']
    X = df[features]
    y = df['success']

    return X, y, df

if __name__ == "__main__":
    movies, credits = load_data()
    X, y, df = preprocess_data(movies, credits)
    print("Preprocessing complete. Shape:", X.shape)
    print("Success distribution:", y.value_counts())
