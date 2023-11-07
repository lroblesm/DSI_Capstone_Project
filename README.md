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

#### Example Output Image from the initial training of the model (25 Epochs)
<img src="./Presentation/Presentation Images/Readme_Image (1).jpg"/>

#### Please refer to the [Executive_Summary](./Executive_Summary.md) for the key insights and recommendations of this project. 
---

## Data
Yolov8 models accept images in .bmp, .dng, .jpeg, .jpg, .mpo, .png, .tif, .tiff, .webp, and .pfm formats [source](https://docs.ultralytics.com/modes/predict/#images). The images used to train this model are satellite images with both .png and .jpg encoding and of a 640 by 640 pixel size. This model performs much better with larger pixel sizes, but can accept images of varying sizes per input. 

### Data Acquisition, Ingestion and Cleaning 

#### Source Data:
The training, validation and test data originated from [Roboflow Universe Data](https://universe.roboflow.com/roboflow-universe-projects/buildings-instance-segmentation/dataset/2). 

The data was then fed to the roboflow [annotation tool](https://roboflow.com/annotate). This tool returns the training, validation and test sets with a corresponding text file for each image; containing information about each class box and mask within the image.

The web interface is then able to resize the images for best practices of different models as well as generate various augmentations to aid in the model training process. 

The data may be downloaded into a zip file or loaded directly onto the notebook with the following code:

To protect your API key load it into your notebook with getpass library
<img src="./Presentation/Presentation Images/Loading_Roboflow_Key.png">

Then define the project, and dataset version
<img src="./Presentation/Presentation Images/code_to_grab_data.png">



You may follow this link to obtain a roboflow API key. 
---

## Requirements for Running the Code

#### Google Colab Environment:

I recommend that you work in google colab while training or running inferences with a yolov8 segmentation model as I encountered runtime errors at the tail end of the training process while working in an AWS [EC2](https://aws.amazon.com/ec2/instance-types/) instance as well as my local computer unless I cloned the google colab virtual environment onto that platform (Keep reading for more details). 

To run the modeling and prediction python notebooks in this repository using google colab simply run ```!pip install ultralytics``` 


#### Hosting the app from local computer:
---
## Table of Contents
### &nbsp;&nbsp;A)[Coding_Notebooks]()
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1)[]()
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2)[]()
### &nbsp;&nbsp;A)[Datasets]()
### &nbsp;&nbsp;A)[Models]() 
### &nbsp;&nbsp;A)[Presentation]() 
### &nbsp;&nbsp;A)[Executive_Summary]()
---
## Contact Information

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*[Lorena Robles](https://www.linkedin.com/in/lroblesm/)