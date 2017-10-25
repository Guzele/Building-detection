import cv2
import numpy as np

from os import listdir
from os.path import isfile, join, splitext


#returns width and height of image
def getBounds(imageName):
    image = cv2.imread(imageName)
    height, width, channels = image.shape 
    return (height, width)

file = open("positives.dat", "w")

train_dir = 'pos/train'

for train_file in listdir(train_dir):
       full_name  = train_dir + '/' + train_file
       w, h = getBounds(full_name)
       file.write (full_name + ' ' + '1 0 0 ' + str(w) + ' ' + str(h) + '\n')
file.close()
       


