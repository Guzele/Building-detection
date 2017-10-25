import cv2
import numpy as np
from matplotlib import pyplot as plt

cascade = "windows_cascade.xml"
detector = cv2.CascadeClassifier(cascade)

#we suppose that image preprocessed
def detectWindows(image):
   return detector.detectMultiScale(image, scaleFactor=1.3,
	minNeighbors=25, minSize=(30, 30), maxSize = (100,100) ) #minNeighbors=10, minSize=(75, 75)


