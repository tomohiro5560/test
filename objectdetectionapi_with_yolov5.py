# -*- coding: utf-8 -*-
"""ObjectDetectionAPI with YOLOv5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BHgXq4R-pOEjBTvVFWuuu8tDJuz-jXP7
"""

!wget https://github.com/ultralytics/yolov5/releases/download/v1.0/coco128.zip
!unzip coco128.zip

!git clone https://github.com/ultralytics/yolov5

!wget https://github.com/ultralytics/yolov5/releases/download/v5.0/yolov5x.pt



# Commented out IPython magic to ensure Python compatibility.
# tensorboardの表示
# %load_ext tensorboard
# %tensorboard --logdir runs



!python /content/yolov5/train.py --img 640 --batch 16 --epochs 300 --data /content/yolov5/data/coco128.yaml --weights /content/yolov5x.pt

!bash /content/yolov5/weights/download_weights.sh

!pip install -r /content/yolov5/requirements.txt

import utils

from utils.google_utils import attempt_download

!pip install attempt_download

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

!pip install tf-object_detection

!wget http://images.cocodataset.org/zips/test2017.zip

!unzip "test2017.zip"

!cp /content/test2017/000000000001.jpg /content/yolov5/data/images

/content/test2017/000000000016.jpg
/content/test2017/000000000019.jpg
/content/test2017/000000000057.jpg
/content/test2017/000000000063.jpg
/content/test2017/000000000069.jpg
/content/test2017/000000000080.jpg
/content/test2017/000000000090.jpg

!cp /content/test2017/000000000001.jpg /content/yolov5/data/images
!cp /content/test2017/000000000019.jpg /content/yolov5/data/images
!cp /content/test2017/000000000057.jpg /content/yolov5/data/images
!cp /content/test2017/000000000063.jpg /content/yolov5/data/images
!cp /content/test2017/000000000069.jpg /content/yolov5/data/images
!cp /content/test2017/000000000080.jpg /content/yolov5/data/images
!cp /content/test2017/000000000090.jpg /content/yolov5/data/images

#000000014408.jpg
!cp /content/test2017/000000014408.jpg /content/yolov5/data/images

!python /content/yolov5/detect.py --source /content/yolov5/data/images/image --weights /content/yolov5x.pt --conf 0.50

