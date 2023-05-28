from tensorflow.keras.models import load_model
import tensorflow as tf
import base64
import io
from PIL import Image
import numpy as np


model = load_model('model.h5')


def run_tensorflow_model(drawing_data):
    # Decode the base64 string into bytes
    image_bytes = base64.b64decode(drawing_data.split(',')[1])
    
    # Read the image from bytes
    image = Image.open(io.BytesIO(image_bytes))

    # Convert the image to grayscale
    grayscale_image = image.convert('L')
    
    # Preprocess the image
    # resized_image = image.resize((28, 28)) # this one gives error due to larger shape (grayscale conversion reduces dimension)
    resized_image = grayscale_image.resize((28, 28))
    image_array = tf.keras.preprocessing.image.img_to_array(resized_image)
    image_array = image_array / 255.0  # Normalize pixel values to [0, 1]
    processed_image = tf.expand_dims(image_array, axis=0)
    
    # Perform prediction
    result = model.predict(processed_image)

    probs = result[0].tolist()
    print(probs)
    digit = probs.index(max(probs))
    
    return str(digit)