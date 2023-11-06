# Importing necessary libraries
import streamlit as st
from PIL import Image as im
import numpy as np
from matplotlib import pyplot as plt
from ultralytics import YOLO


# Loading production model, which is the current best/last trained model
production_model = YOLO('25_epochs.pt')

# Definining a function to preprocess the input image
def preprocess_input_image(image):
    img = im.open(image)
    img = np.array(img)
    return img

st.title("Semantic Segmentation of Satellite Images")

# Function to upload and make predictions on the image
input_image = st.file_uploader("Upload a JPG or PNG Satellite Image ", type=["jpg", "jpeg", "PNG"])
# This activates the function the moment a picture is uploaded:
if input_image is not None:
    st.image(input_image, caption="Upload Complete", use_column_width=True)
    st.write("")
    if st.button("Process"):
        st.write("Processing...")
       
        # Calling on the function to preprocess the uploaded image
        processed_input = preprocess_input_image(input_image)
        
        # This code returns the inference from the model on the input image
        test_result = production_model.predict(processed_input, conf=0.2, save=True) #This confidence threshold was the best balance I found.
        test_result_array = test_result[0].plot()                                    # as the model still needs to train,
        prediction = im.fromarray(test_result_array)                                 # I am not including the option to change it in the app, for now.
        st.image(prediction, use_column_width='always')
        st.write('Process Complete')
