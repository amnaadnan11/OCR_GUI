from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get the drawing data from the canvas
    drawing_data = request.form['imageData']

    # Perform prediction using TensorFlow model
    prediction = run_tensorflow_model(drawing_data)

    # Return the prediction result
    return prediction


if __name__ == '__main__':
    app.run(debug=True)
