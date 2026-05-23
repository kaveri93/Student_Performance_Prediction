'''
this file is for backend
'''
import flask
import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the trained model
with open("Model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form data
        Hours_Studied = float(request.form['Hours_Studied'])
        Previous_Scores = float(request.form['Previous_Scores'])
        Extracurricular_Activities = int(request.form['Extracurricular_Activities'])
        Sleep_Hours = float(request.form['Sleep_Hours'])
        Sample_Question_Papers_Practiced = float(request.form['Sample_Question_Papers_Practiced'])

        # Prediction
        prediction = model.predict([[Hours_Studied, Previous_Scores, Extracurricular_Activities,
                                     Sleep_Hours, Sample_Question_Papers_Practiced]])[0]

        return render_template('index.html', prediction_text=f"Predicted Performance Index: {prediction:.2f}")
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
