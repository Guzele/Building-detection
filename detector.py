import cv2
import numpy as np
from matplotlib import pyplot as plt

from buildingDetector import detectHouses, countourHouses
from windowsDetector import detectWindows

from number_floors import number_floors
from color_detection import *

def printMessage(image, message, coord):
    cv2.putText(image, message, (20, coord),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 5)
    cv2.putText(image, message,  (20, coord),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)
def cropImage(image, rect):
     x, y, w, h = rect
     return image[y: y + h, x: x + w]
     
def detectAll(imageName):
    
    coord = 15
    image_full, image, buildings = detectHouses(imageName)
    '''for x, y, w, h in buildings: 
        cv2.rectangle(image_full, (x, y), (x + w, y + h), (0, 0, 0), 2)'''
    
    if len(buildings) == 0:
        printMessage(image_full, 'No buildings detected', coord)
        cv2.imshow("Buildings", image_full)
        cv2.waitKey(0)
        return
    else:
        countourHouses(image_full, buildings, (153, 0, 153))
    
    for (num_of_building, building) in enumerate(buildings):
         #crop image for window detection
         cropped_image_full = cropImage(image_full, building)
         cropped_image = cropImage(image, building)
         
         windows = detectWindows(cropped_image)

         for  x, y, w, h in windows:
	     cv2.rectangle(cropped_image_full, (x, y), (x + w, y + h), (0, 0, 255 ), 2)
        
         num_floors = number_floors(windows)
         color = color_detection(windows,cropped_image_full)

         #print '#' + str (num_of_building+1) + ': floors: ' + str (num_floors)
         # '#' + str (num_of_building) + ': floors: ' + str (num_floors)
         printMessage(image_full,"{}) floors: {}".format(num_of_building+1, num_floors), coord)
         coord += 20
         printMessage(image_full, "{}) color: {}".format(num_of_building+1, color), coord)
         coord += 40

    cv2.imshow("Buildings", image_full)
    cv2.waitKey(0)

