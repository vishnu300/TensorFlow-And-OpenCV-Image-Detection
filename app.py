import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import pickle


import streamlit as st

# Your CSS code

# Rest of your Streamlit app code


# Load the model
model = pickle.load(open('image_cls_ply.joblib', 'rb'))

# Define image dimensions (replace with your model's input size)
image_width = 180
image_height = 180

# Function to preprocess the image and make a prediction
def predict_image(img_path, class_names):
  img = tf.keras.utils.load_img(img_path, target_size=(image_height, image_width))
  img_array = tf.keras.utils.array_to_img(img)
  img_array = np.expand_dims(img_array, axis=0)
  predictions = model.predict(img_array)
  predicted_probabilities = tf.nn.softmax(predictions[0]).numpy()
  predicted_class_index = np.argmax(predicted_probabilities)
  predicted_class_name = class_names[predicted_class_index]
  return predicted_class_name, predicted_probabilities

# Streamlit App
st.header('Image Classification')

# Allow user to upload an image
img_file = st.file_uploader("Upload your image here...")

if img_file is not None:
  # Load the class names from your dataBase object (assuming it's defined)
  class_names = ['MESSI','maria_sharapova','Roger_Federer','Serena_Williams','VIRAT_KOLI']  # Replace with your class name loading logic

  # Read the uploaded image
  img = image.load_img(img_file, target_size=(image_height, image_width))
  st.image(img, width=250)  # Display the uploaded image

  # Make prediction
  predicted_class, probabilities = predict_image(img_file, class_names)

  # Display results
  st.success(f'Predicted Class: {predicted_class}')
  st.text(f'Probabilities: {probabilities}')

