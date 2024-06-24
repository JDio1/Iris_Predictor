import joblib
import numpy as np
from flask import Flask, request, jsonify
from sklearn.ensemble import RandomForestClassifier  # Example import from scikit-learn


app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict(np.array(data['input']).reshape(1, -1))
    return jsonify({'prediction': int(prediction[0])})

if __name__ == "__main__":
    # Ensure the app listens on port 8080
    app.run(host='0.0.0.0', port=8080)