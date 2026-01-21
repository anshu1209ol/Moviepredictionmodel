import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
from preprocess import load_data, preprocess_data

def train_model():
    movies, credits = load_data()
    X, y, df = preprocess_data(movies, credits)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Save model
    import os
    model_path = os.path.join(os.environ['TEMP'], 'model.pkl')
    joblib.dump(model, model_path)
    print(f"Model saved as {model_path}")

if __name__ == "__main__":
    train_model()
