from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the pre-trained model
# Ensure 'iris_model.pkl' exists in the same directory
MODEL_PATH = 'iris_model.pkl'

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

@app.route('/')
def home():
    """Health check endpoint to verify the server is live."""
    return jsonify({
        "status": "Model is Online",
        "version": "1.1",
        "model_loaded": model is not None
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Prediction endpoint for the Iris dataset."""
    if model is None:
        return jsonify({"error": "Model file not found"}), 500

    try:
        data = request.get_json()
        # Expecting JSON: {"features": [5.1, 3.5, 1.4, 0.2]}
        features = np.array(data['features']).reshape(1, -1)
        
        prediction = model.predict(features)
        
        return jsonify({
            'prediction': int(prediction[0]),
            'status': 'success'
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # We use 0.0.0.0 so it's accessible inside the Docker container
    app.run(host='0.0.0.0', port=5000)
