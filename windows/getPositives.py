import cv2
import numpy as np

from os import listdir
from os.path import isfile, join, splitext

import detect_rectangles as dr

#returns bounds of windows in the image by its name and dataset path
#color is color by which labeled image was marked
def getBounds(filename, path, color):
    full_filename = filename + '.png'
    full_path = path + '/labels'
    labeled_image = full_path + '/' + full_filename
    
    #a = full_path + '/' + filename + '-winmask.png'
    #img = cv2.imread(a)
    #b = full_path + '/' + filename + '.png'
    #cv2.imwrite(b, img)

    #print labeled_image
    return dr.detectRect(labeled_image, color)


file = open("positives.dat", "w")

dirs = [('graz50_facade_dataset', 'red')] # ('tsg60', 'white') ('cvpr', 'red')
for dataset, color in dirs:
   dataset_dir = 'pos/' + dataset
   train_dir = dataset_dir + '/train'
   # names with extension of training examples
   train_files = [f for f in listdir(train_dir) if isfile(join(train_dir, f))]

   for filename_extension in train_files:
       filename, file_extension = splitext(filename_extension)
       #train_dirname + '/' + full_filename
       rects = getBounds(filename, dataset_dir, color)
       file.write (train_dir + '/' + filename_extension + ' ' + str(len(rects))) #
       for rect in rects:
           x, y, w, h = rect
           file.write ('  ' + str(x) + ' ' + str(y) +  ' ' + str(w) + ' ' + str(h))
           #break
       file.write ('\n') 
       #break
       #print rects
       '''if  len(rects) > 20 :
            print len(rects)
            print filename'''
file.close()
       


