from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Load model if exists
model_path = os.path.join(os.environ['TEMP'], 'model.pkl')
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not found. Please train the model first by running python scripts/train_model.py'}), 400

    data = request.json
    budget = data.get('budget', 1000000)
    popularity = data.get('popularity', 10.0)
    runtime = data.get('runtime', 120)
    vote_average = data.get('vote_average', 5.0)
    vote_count = data.get('vote_count', 100)
    genre_count = data.get('genre_count', 3)
    cast_size = data.get('cast_size', 10)

    input_data = pd.DataFrame([[budget, popularity, runtime, vote_average, vote_count, genre_count, cast_size]],
                              columns=['budget', 'popularity', 'runtime', 'vote_average', 'vote_count', 'genre_count', 'cast_size'])
    prediction = model.predict(input_data)[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
