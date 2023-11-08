# **EXECUTIVE SUMMARY**

According to the [Satellite Imaging Corporation (SIC)](https://www.satimagingcorp.com/about/), the combination of aerial, satellite imagery, machine learning algorithms, and GIS management systems are crucial for the future of the following kinds of applications and much more ([source1](https://www.satimagingcorp.com/applications/environmental-impact-studies/urban-planning/), [source2](https://www.satimagingcorp.com/)): 

    Updating information on road networks and other urban infrastructure
    Collection and analysis of data on population density, distribution, and growth
    Preparation of housing typologies
    Analysis of watersheds
    Landscape development
    3D modeling
    Infrastructure modeling
    Environmental impact assessment
    Carbon footprint

### Example SIC Project: 
<img src="./Presentation/Presentation Images/SIC_Automated_Building_Footprint_Extraction.png">

This machine/deep learning project is an example of how the tools to provide the services of a corporation such as SIC would be developed. Image segmentation returns information about the exact pixels of an object which can then be used to convert into units of measure such as meters; to then analyze urban landscape morphology in very effective ways. 

 
## Data Science & Machine Learning Process

For this project I have chosen to train an image segmentation model that has not been utilized for analyzing satellite imagery to gain an more intimate understanding of the process.

### Model Performance

Yolo models are evaluated using the following metrics [(source)](https://docs.ultralytics.com/guides/yolo-performance-metrics/#introduction): 

    Mean Average Precision (mAP): Calculates the average precision values across multiple object classes over multiple intersection vs. union measures.
            Intersection over Union (IoU): IoU is a measure that quantifies the overlap between a predicted bounding box and a ground truth bounding box. It plays a fundamental role in evaluating the accuracy of object localization.
                                        IoU= Area of Overlap / Area of Union

    Precision and Recall: Precision quantifies the proportion of true positives among all positive predictions, assessing the model's capability to avoid false positives. On the other hand, Recall calculates the proportion of true positives among all actual positives, measuring the model's ability to detect all instances of a class.

    F1 Score: The F1 Score is the harmonic mean of precision and recall, providing a balanced assessment of a model's performance while considering both false positives and false negatives.

For this project I am seeking to optimize for mAP as it requires IOU, Precision, Recall, Precision Recall Curve, and AP; and it is the standard for most segmentation applications. 

<img src="./Presentation/Presentation Images/Formulas.png">

### Below are the evaluations metrics for the model trained after 50 epochs and 100 epochs: 

Note: B is for detection and M is for segmentation. Also mAP50 puts the IoU threshold at .5 while mAP50-90 averages mAP over different IoU thresholds, from 0.5 to 0.95 [source](https://www.cs.cornell.edu/%7Esbell/pdf/cvpr2016-ion-bell.pdf]).

<img src="./Presentation/Presentation Images/results.png">
<img src="">


### Computational Expense:

Because this model had never been trained on satellite images the initial computational expense was quite high. The first round of training with 35 epochs took a little over 15 hours. However the training speed did improve tremendously over time. The second round of training with 15 epochs took 3.5 hours. So, at this point I decided that I could afford to train the model for another 200 epochs before the project's final submission. 

---
## **Conclusions & Future Steps**

This project has been developed as part of the General Assembly's Data [Science Immersive Program](https://generalassemb.ly/education/data-science-immersive?topic=&mkt_account_id=1056949875&mkt_campaign_id=20419406360&mkt_ad_group_id=&mkt_device_type=c&mkt_keyword=&mkt_matchtype=&mkt_placement=&mkt_ad_id=&mkt_network=x&mkt_target_id=&mkt_feed_item_id=&utm_source=google&utm_medium=display-rem&utm_campaign=TS:TX:NBR:USA:TCLS:AllCourses:PMAX2&utm_content=campus-lead-lander&utm_term=&gclid=CjwKCAiA3aeqBhBzEiwAxFiOBmWq7wzqzD3j8kRj4eXCQQws1bTdEV87EvUWhSmaNsw5eF-NPdWqbBoCd50QAvD_BwE&gclsrc=aw.ds). 

My motivations for this project comes from my desire to make a career shift into the field of urban planning/civil engineering to help develop more equitable, sustainable and resilient communities. My newly trained model's performance has a long way to go before it could be used in any meaningful way; but provided a valuable learning experience. Given what I have learned about various convolutional neural networks 

### More training
To improve the performance of the model over time, I will continue to find and/or develop more training data and transform it to fit the requirements of the yolov8 model. Some examples would be the [Massachusetts Roads Dataset](https://www.cs.toronto.edu/~vmnih/data/) and the [Inria Arial Image Labeling Dataset](https://project.inria.fr/aerialimagelabeling/).

In addition I will perform different types of [augmentations](https://towardsdatascience.com/complete-guide-to-data-augmentation-for-computer-vision-1abe4063ad07)-a technique used to artificially increase dataset size- on the data which may include; cropping, rotating, flipping, blurring, and changing the saturation of different colors. 

### Hyperparameter tuning
Hyperparameters are high-level, structural settings for the algorithm which are set before the model begins training. Some hyperparameters of interest for my model are [(source)](https://docs.ultralytics.com/guides/hyperparameter-tuning/#what-are-hyperparameters): 

    Image size: Typically larger is better, so I might create my own high quality dataset with fewer images but larger image sizes.

    Batch size: Determines the number of samples processed before the model updates its weights. I tried a size of 4 and a size of 6. Training with a batch size of 6 was much faster than the size 4; so I will try to figure out how high I can go before it is no longer computationally beneficial.  

    Learning Rate lr0: Determines the step size at each iteration while moving towards a minimum in the loss function. The model automatically selected a learning rate of .001. 
    
    Optimizer: Adjust the model's parameters during training to minimize a loss function.My model automatically picked an AdamW optimizer, which according to the [Ultralytics forum](https://github.com/ultralytics/ultralytics/issues/3360) it seems as though the model tends to choose this optimizer when the dataset is on the smaller side. So I would like to do more research on the topic to choose one or two more optimizer to test.

    Architecture Specifics: Such as channel counts, number of layers, types of activation functions, etc.These show up in the YAML document generated while training the model and can be used to initialize future trainings.My plan is to compare these parameters from the YAML documents of the three models I have saved.  

These are steps I did not attempt during the first few training sessions as the documentation clearly states they are all highly computationally intensive and I had limited time to complete the project. Also Yolo models use a _mutate method for hyperparameter tuning. This means you need to test sets of hyperparameters one at a time and compare them one to one using the tune csv and scatter plots generated. 