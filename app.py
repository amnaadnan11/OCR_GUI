from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np

from model import run_tensorflow_model

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# static files to export css
@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

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
