<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  
</head>
<body>
  <h1>🚀 Student Performance Prediction — OOP Implementation with Flask Deployment</h1>

  <h2>📑 Table of Contents</h2>
  <ul>
    <li>Project Overview</li>
    <li>What is Multiple Linear Regression?</li>
    <li>Mathematical Foundation</li>
    <li>Dataset Description</li>
    <li>Project Structure</li>
    <li>OOP Design — The StudentPerformance Class</li>
    <li>Code Walkthrough — main.py</li>
    <li>Exception Handling</li>
    <li>Model Persistence with Pickle</li>
    <li>Flask Web Application — app.py</li>
    <li>Frontend — templates/index.html</li>
    <li>Evaluation Metrics</li>
    <li>Installation & Usage</li>
    <li>How to Run</li>
    <li>Sample Prediction</li>
    <li>Technologies Used</li>
    <li>Contact & Support</li>
  </ul>

  <h2>📌 Project Overview</h2>
  <p>
    This project demonstrates how to build a Multiple Linear Regression (MLR) model in a clean, maintainable, and production-ready way using Object-Oriented Programming (OOP) principles in Python. The model predicts a student’s <strong>Performance Index</strong> based on study hours, previous scores, extracurricular activities, sleep hours, and practice of sample question papers. 
  </p>
  <p>
    The pipeline includes data preprocessing, training, testing, manual accuracy calculation, prediction on custom inputs, and model persistence using pickle. A Flask web application serves predictions through an interactive HTML/CSS frontend, allowing users to input student details and instantly receive predictions.
  </p>

  <h2>🧠 What is Multiple Linear Regression?</h2>
  <p>
    Multiple Linear Regression (MLR) models the relationship between one dependent variable and multiple independent variables. Unlike Simple Linear Regression, MLR captures the combined influence of several predictors.
  </p>
  <p>Real-world use cases include predicting exam scores, house prices, startup profits, and employee salaries.</p>

  <h2>📐 Mathematical Foundation</h2>
  <p>
    The MLR equation:
    <br><code>y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε</code>
  </p>
  <p>
    For this project:
    <br><code>Performance Index = β₀ + β₁(Hours Studied) + β₂(Previous Scores) + β₃(Extracurricular) + β₄(Sleep Hours) + β₅(Sample Papers)</code>
  </p>
  <p>
    Coefficients are estimated using Ordinary Least Squares (OLS), minimizing the sum of squared residuals.
  </p>

  <h2>📊 Dataset Description</h2>
  <p>File: <code>Student_Performance.csv</code></p>
  <table>
    <tr><th>Column</th><th>Type</th><th>Description</th></tr>
    <tr><td>Hours Studied</td><td>Float</td><td>Study hours per day</td></tr>
    <tr><td>Previous Scores</td><td>Float</td><td>Past exam scores</td></tr>
    <tr><td>Extracurricular Activities</td><td>String → Integer</td><td>Yes=1, No=0</td></tr>
    <tr><td>Sleep Hours</td><td>Float</td><td>Average sleep per day</td></tr>
    <tr><td>Sample Papers Practiced</td><td>Integer</td><td>Number of practice papers</td></tr>
    <tr><td>Performance Index</td><td>Float</td><td>Target variable</td></tr>
  </table>

  <h2>🗂️ Project Structure</h2>
  <ul>
    <li><code>main.py</code> — Core ML pipeline using OOP</li>
    <li><code>app.py</code> — Flask backend for web prediction</li>
    <li><code>Student_Performance.csv</code> — Dataset</li>
    <li><code>Model.pkl</code> — Trained & serialized model</li>
    <li><code>templates/index.html</code> — Frontend HTML form</li>
    <li><code>README.html</code> — Project documentation</li>
  </ul>

  <h2>🏗️ OOP Design — The StudentPerformance Class</h2>
  <p>Encapsulates the ML pipeline: data loading, training, testing, prediction, and saving.</p>
  <p>Principles applied: Encapsulation, Abstraction, Single Responsibility, Constructor Initialization.</p>

  <h2>🔍 Code Walkthrough — main.py</h2>
  <p>Includes methods for training, testing, manual R² calculation, prediction on custom inputs, and saving/loading the model with pickle.</p>

  <h2>🛡️ Exception Handling</h2>
  <p>Each method uses try-except with detailed diagnostics (line number, error type, message).</p>

  <h2>💾 Model Persistence with Pickle</h2>
  <p>Models are serialized to <code>Model.pkl</code> and reloaded for fast predictions without retraining.</p>

  <h2>🌐 Flask Web Application — app.py</h2>
  <p>Routes:</p>
  <table>
    <tr><th>Route</th><th>Method</th><th>Description</th></tr>
    <tr><td>/</td><td>GET</td><td>Renders input form</td></tr>
    <tr><td>/predict</td><td>POST</td><td>Receives form data, runs prediction, returns result</td></tr>
  </table>

  <h2>📈 Evaluation Metrics</h2>
  <p><strong>R² Score:</strong> Measures accuracy (closer to 1 = better).<br>
     <strong>RMSE:</strong> Root Mean Squared Error, penalizes large errors.<br>
     Overfitting/Underfitting detected by comparing train vs test scores.</p>

  <h2>⚙️ Installation & Usage</h2>
  <ol>
    <li>Clone the repository: <code>git clone &lt;repo-url&gt;</code></li>
    <li>Navigate: <code>cd student-performance</code></li>
    <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
  </ol>

  <h2>▶️ How to Run</h2>
  <ol>
    <li>Train the model: <code>python main.py</code></li>
    <li>Launch Flask app: <code>python app.py</code></li>
    <li>Open browser: <code>http://127.0.0.1:5000/</code></li>
    <li>Enter student details and click <strong>Predict Performance</strong>.</li>
  </ol>

   <h2>🎯 Sample Prediction</h2>
  <table>
    <tr><th>Feature</th><th>Value</th></tr>
    <tr><td>Hours Studied</td><td>7</td></tr>
    <tr><td>Previous Scores</td><td>99</td></tr>
    <tr><td>Extracurricular Activities</td><td>1 (Yes)</td></tr>
    <tr><td>Sleep Hours</td><td>9</td></tr>
    <tr><td>Sample Papers Practiced</td><td>1</td></tr>
  </table>
  <p>The model returns a predicted Performance Index based on these inputs.</p>
  <h2>🛠 Technologies Used</h2>
<table>
  <tr><th>Technology</th><th>Version</th><th>Purpose</th></tr>
  <tr><td>Python</td><td>3.8+</td><td>Core programming language</td></tr>
  <tr><td>NumPy</td><td>1.21+</td><td>Numerical computation</td></tr>
  <tr><td>Pandas</td><td>1.3+</td><td>Data manipulation</td></tr>
  <tr><td>scikit-learn</td><td>1.0+</td><td>Machine learning model & metrics</td></tr>
  <tr><td>Flask</td><td>2.0+</td><td>Web framework for deployment</td></tr>
  <tr><td>Pickle</td><td>Built-in</td><td>Model serialization</td></tr>
  <tr><td>HTML & CSS</td><td>Latest</td><td>Frontend design and styling</td></tr>
</table>

<h2>📬 Contact & Support</h2>
<p><strong>Author:</strong> S.Lakshmi Kaveri</p>
<p><strong>Email:</strong>sankathalalakshmikaveri93@gmail.com</p>
<p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/kaveri03/">linkedin.com/in/s-lakshmi-kaveri</a></p>
<p><strong>GitHub:</strong> <a href="https://github.com/kaveri93">github.com/lakshmikaveri</a></p>
<p><strong>Live Demo — [Click Here to View the Application] :</strong> <a href="https://student-performance-prediction-0zl4.onrender.com"></a></p>
<p>This project is open source and available under the MIT License.</p>
<p>Built with ❤️ by Lakshmi kaveri — Python Developer & Machine Learning Enthusiast</p>

