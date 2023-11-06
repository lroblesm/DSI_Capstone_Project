
from PIL import Image as im
import numpy as np
from matplotlib import pyplot as plt
from ultralytics import YOLO
import anvil.server
import anvil.media
import io

with open("../Uplink_Key.txt", 'r') as fin:
  uplink_key = fin.read().strip()

anvil.server.connect(uplink_key)

production_model = YOLO('../Models/25_epochs')
   
@anvil.server.callable
def predict_function(file):
  with anvil.media.TempFile(file) as filename:
        image = load_img(filename)
  test_result = production_model.predict(image, conf=0.2, save=True)
  test_result_array = test_result[0].plot()
  img = im.fromarray(test_result_array)
  bs = io.BytesIO()
  name = "prediction_image"
  img.save(bs,format="JPEG")
  return anvil.BlobMedia('image/jpeg', bs.getvalue(), name=name)

anvil.server.wait_forever()