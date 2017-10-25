import cv2
import buildingDetector as det2
import numpy as np
from os import listdir,chdir
    
def check_neg(train_dir, isShow = False):
   false_detect = 0
   not_detect = 0
   for train_file in listdir(train_dir):
       full_name  = train_dir + '/' + train_file
       image_full, image, rects = det2.detectHouses(full_name, True)
       if len(rects) ==0:
         not_detect = not_detect + 1
         continue
       false_detect = false_detect + 1
       if isShow:
           countourHouses(image_full, rects)
           cv2.imshow("Housess", image_full)
           cv2.waitKey(0)
   return (false_detect, not_detect)

def check_pos(train_dir, isShow = False):
   good = 0
   bad = 0
   for train_file in listdir(train_dir):
       full_name  = train_dir + '/' + train_file
       image_full, image, rects = det2.detectHouses(full_name, True)
       if len(rects) ==0:
         bad  = bad + 1
       else:
         good = good + 1
       if isShow:
           countourHouses(image_full, rects)
           cv2.imshow("Housess", image_full)
           cv2.waitKey(0) 
   return (good, bad)
 
def sumup(detect, notdetect):
   total = detect + notdetect
   print 'Detected: ' + str(detect)
   print 'Not detected: ' + str(notdetect)
   print 'Total: ' + str(total) 
   print 'Percentage of Detected ' + str (float(detect) / total) + '\n' 


chdir('buildings')

'''print 'Negatives'
false_detect, not_detect = check_neg('neg')
false_detect1, not_detect1 = check_neg('jpg')
sumup (false_detect + false_detect1, not_detect + not_detect1)

det, notdet = check_pos('pos/test')
print 'Positives test'
sumup(det, notdet)''' 

det, notdet = check_neg('additional/neg')
print 'Additional neg'
sumup(det, notdet)

det, notdet = check_pos('additional/pos')
print 'Additional pos'
sumup(det, notdet)





    



