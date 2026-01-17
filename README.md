# Movie Success Prediction System

## Problem Statement
To design an automated system that predicts movie success using historical data.

## Objective
Build a machine learning model that accepts movie details as input and predicts whether the movie will be a Hit, Average, or Flop.

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Streamlit
- Kaggle Dataset (TMDB 5000 Movie Dataset)

## Functional Requirements
- Accept movie details as input (budget, popularity, runtime, vote_average, vote_count, genre_count, cast_size)
- Predict movie success (Hit / Average / Flop)
- Display prediction result clearly

## Non-Functional Requirements
- Easy to use (Streamlit web interface)
- Accurate prediction (Model trained on historical data)
- Fast response time (Real-time prediction)

## Requirements Fulfillment
- [x] Accepts movie details as input
- [x] Predicts success categories
- [x] Displays results clearly
- [x] Easy to use interface
- [x] Uses historical data for training
- [x] Fast response time

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run preprocessing: `python scripts/preprocess.py`
3. Train model: `python scripts/train_model.py`
4. Run app: `streamlit run app.py`
