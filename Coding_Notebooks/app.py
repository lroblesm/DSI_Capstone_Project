import streamlit as st
from PIL import Image as im
import numpy as np
from matplotlib import pyplot as plt
from ultralytics import YOLO


st.title('Building Segmentation')

input_image = st.file_uploader(label='Upload satellite image')

production_model = YOLO('../Models/25_epochs')

test_result = production_model.predict(input_image, conf=0.2, save=True)
test_result_array = test_result[0].plot()
st.image(img, use_column_width='always')

# img = im.fromarray(test_result_array)
# st.image(test_result_array)