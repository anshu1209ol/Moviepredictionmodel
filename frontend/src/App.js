import React, { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    budget: 1000000,
    popularity: 10.0,
    runtime: 120,
    vote_average: 5.0,
    vote_count: 100,
    genre_count: 3,
    cast_size: 10
  });
  const [prediction, setPrediction] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: parseFloat(e.target.value)
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });
      const data = await response.json();
      if (data.error) {
        setPrediction(data.error);
      } else {
        setPrediction(`Predicted Success: ${data.prediction}`);
      }
    } catch (error) {
      setPrediction('Error: Could not connect to the server');
    }
  };

  return (
    <div className="App">
      <h1>Movie Success Prediction</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Budget ($):
          <input type="number" name="budget" value={formData.budget} onChange={handleChange} />
        </label>
        <label>
          Popularity:
          <input type="number" step="0.1" name="popularity" value={formData.popularity} onChange={handleChange} />
        </label>
        <label>
          Runtime (minutes):
          <input type="number" name="runtime" value={formData.runtime} onChange={handleChange} />
        </label>
        <label>
          Vote Average:
          <input type="number" step="0.1" min="0" max="10" name="vote_average" value={formData.vote_average} onChange={handleChange} />
        </label>
        <label>
          Vote Count:
          <input type="number" name="vote_count" value={formData.vote_count} onChange={handleChange} />
        </label>
        <label>
          Number of Genres:
          <input type="number" name="genre_count" value={formData.genre_count} onChange={handleChange} />
        </label>
        <label>
          Cast Size:
          <input type="number" name="cast_size" value={formData.cast_size} onChange={handleChange} />
        </label>
        <button type="submit">Predict</button>
      </form>
      {prediction && <p>{prediction}</p>}
    </div>
  );
}

export default App;
