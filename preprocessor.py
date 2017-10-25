import cv2
import numpy as np
from matplotlib import pyplot as plt

def preprocess(imageName):
   image =  cv2.imread(imageName)
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   #histogram equalization, for different light conditions
   image_histogram = cv2.equalizeHist(gray)
   return image_histogram

