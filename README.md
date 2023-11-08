># Semantic Segmentation of Buildings in Stellite Images
>### By Lorena Robles
---

## Project Overview

Semantic Segmentation is a deep learning algorithm that associates a label or category with every pixel in an image.
It allows the object of interest to span multiple areas in the image at the pixel level. It also detects objects that are irregularly shaped, in contrast to object detection, where objects must fit within a bounding box. 

It also differs from instance segmentation in that it does not differentiate specific instances of a category/class; so the behaviors and distributions of all instances of a category/class may be analysis globally. 

>### Project Objective
>
>**To train the newly developed Yolov8 segmentation model for segmentation of buildings using satellite images.** 

YOLOv8 is a group of convolutional neural network models, created and trained using the PyTorch framework

It was trained on images from the COCO(Common Objects in Context) [dataset](https://tech.amikelive.com/node-718/what-object-categories-labels-are-in-coco-dataset/)

Categories for this model included common objects and animals, so this particular model has not been trained on satellite images. 

Case uses for semantic segmentation of satellite images include land use analysis to aid in urban planning decisions, identifying damage during natural disasters, and natural resource mapping for sustainability planning and biodiversity conservation ([source_1](https://keymakr.com/blog/semantic-segmentation-uses-and-applications/), [source_2](https://www.pnas.org/doi/10.1073/pnas.2109217118)).

#### Example Output Image from the initial training of the model (25 Epochs):
<img src="./Presentation/Presentation Images/Readme_Image (1).jpg"/>

#### Please refer to the [Executive_Summary](Executive_Summary.md) for the key insights and recommendations of this project. 
---

## Data
Yolov8 models accept images in .bmp, .dng, .jpeg, .jpg, .mpo, .png, .tif, .tiff, .webp, and .pfm formats [source](https://docs.ultralytics.com/modes/predict/#images). The images used to train this model are satellite images with both .png and .jpg encoding and of a 640 by 640 pixel size. This model performs much better with larger pixel sizes, but can accept images of varying sizes per input. 

### Data Acquisition, Ingestion and Cleaning 

#### Source Data:
The training, validation and test data originated from [Roboflow Universe Data](https://universe.roboflow.com/roboflow-universe-projects/buildings-instance-segmentation/dataset/2). 

The dataset contains:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 13,528 Train Images, 82%
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1,934 Validation Images, 12%
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 967 Test Images, 6%

The dataset was then fed to the roboflow [annotation tool](https://roboflow.com/annotate). This tool returns the training, validation and test sets with a corresponding text file for each image; containing information about each class box and mask within the image.

The web interface is then able to resize the images for best practices of different models as well as generate various augmentations to aid in the model training process. 

The data may be downloaded into a zip file or loaded directly onto the notebook with the following code:

To protect your API key load it into your notebook with getpass library
<img src="./Presentation/Presentation Images/Loading_Roboflow_Key.png">

Then define the project, and dataset version
<img src="./Presentation/Presentation Images/code_to_grab_data.png">

You may follow this [link](https://docs.roboflow.com/api-reference/authentication) to learn how to obtain a roboflow API key. 

---

## Requirements for Running the Code

#### Google Colab Environment:

I recommend that you work in google colab while training or running inferences with my pre-trained yolov8 segmentation model as I encountered runtime errors (as of Nov. 2023) while working in an AWS [EC2](https://aws.amazon.com/ec2/instance-types/) instance as well as my local computer unless I cloned the google colab virtual environment onto that platform.

Another reason for this consideration is the availability of using a free GPU on google colab. 

To run the modeling and prediction python notebooks in this repository using google colab simply run ```!pip install ultralytics``` from your notebook.


#### Hosting the app from a local computer:
This project contains a very simple [app](./Coding_Notebooks/app.py) to run inferences on the trained model by uploading any satellite image. I recommend satellite images are zoomed into a scale between 100-50 meters. 

To host the app locally you may need to clone the original google colab environment. To  create a copy of the google colab virtual environment used for this project run `!Pip install -r requirements.txt` in a notebook inside your new environment. 

To run the app download the app.py document navigate to it's location inside your command line interface and type `streamlit run app.py`


---
## Table of Contents
### &nbsp;&nbsp;A)[Coding_Notebooks](./Coding_Notebooks/)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1)[app.py](./Coding_Notebooks/app.py)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2)[Model_Predictions_Process](./Coding_Notebooks/Model_Predictions_Process.ipynb)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3)[Satellite_Image_Building_Segmentation_Training_1](./Coding_Notebooks/Satellite_Image_Building_Segmentation_Training_1.ipynb)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4)[Satellite_Image_Building_Segmentation_Training_2](./Coding_Notebooks/Satellite_Image_Building_Segmentation_Training_2.ipynb)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5)[Satellite_Image_Building_Segmentation_Training_3](./Coding_Notebooks/Satellite_Image_Building_Segmentation_Training_3.ipynb)
### &nbsp;&nbsp;A)[Datasets](./Datasets/)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1)[Denver_Metro_Area_Prediction_Images](./Datasets/Denver_Metro_Area_Prediction_Images/)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2)[Original_Dataset_Test_Images_B&W](./Datasets/Original_Dataset_Test_Images_B&W/)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3)[Original_Dataset_Test_Images_Color_1](./Datasets/Original_Dataset_Test_Images_Color_1/)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4)[Original_Dataset_Test_Images_Color_2](./Datasets/Original_Dataset_Test_Images_Color_2/)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5)[Original_Dataset_Test_Images_Color_3](./Datasets/Original_Dataset_Test_Images_Color_3/)
### &nbsp;&nbsp;A)[Trained_Model_Outputs](./Trained_Model_Outputs/) 
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1)[20_Epochs](./Trained_Model_Outputs/20_epochs/)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1)[35_Epochs](./Trained_Model_Outputs/35_epochs/)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1)[50_Epochs](./Trained_Model_Outputs/50_epochs/)
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1)[350_Epochs](./Trained_Model_Outputs/350_Epochs/)
### &nbsp;&nbsp;A)[Presentation](./Presentation/) 
### &nbsp;&nbsp;A)[Executive_Summary](Executive_Summary.md)
---
#### Thanks for visiting! I can be reached on [Linkedin](https://www.linkedin.com/in/lroblesm/)