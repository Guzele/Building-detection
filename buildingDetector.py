import cv2
import numpy as np
from matplotlib import pyplot as plt
from preprocessor import preprocess

cascade = "house_cascade.xml"
detector = cv2.CascadeClassifier(cascade)

def v_detectHouses(image):
   rects = detector.detectMultiScale(image, scaleFactor=1.5,
	minNeighbors= 3, minSize=(200, 200))
   return rects

# loop over buildings and draw a rectangle surrounding each
def countourHouses(image_full, rects, color = (0,0,255)):
   for (i, (x, y, w, h)) in enumerate(rects):
	cv2.rectangle(image_full, (x, y), (x + w, y + h), color, 2)
	cv2.putText(image_full, "House #{}".format(i + 1), (x, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)

def detectHouses(imageName, isPreproccessed = False):
    image_full = cv2.imread(imageName)
    image_full = cv2.resize(image_full,(600, 400))

    image = image_full
    if not isPreproccessed:
       image = preprocess(imageName)
       image= cv2.resize(image,(600, 400))
       
    rects = v_detectHouses(image)
    rects = combineRects(rects)
    return (image_full, image, rects)


def combineRects(rects):
    new_rects = []
    for i in range(len(rects)):
        rect = rects[i]
        j = i + 1
        while (j < len(rects)):
            rect2 = rects[j] 
            if isIntersect(rect, rect2):
                 rect = union(rect, rect2)
            j += 1
        if (not inList(new_rects, rect)):
            new_rects.append(rect)
    return new_rects

def inList(list, rect):
   for e in list:
       if isIntersect(rect,e):
            return True
   return False

def union(a,b):
  x = min(a[0], b[0])
  y = min(a[1], b[1])
  w = max(a[0]+a[2], b[0]+b[2]) - x
  h = max(a[1]+a[3], b[1]+b[3]) - y
  return (x, y, w, h)

def intersection(a,b):
  x = max(a[0], b[0])
  y = max(a[1], b[1])
  w = min(a[0]+a[2], b[0]+b[2]) - x
  h = min(a[1]+a[3], b[1]+b[3]) - y
  if w<0 or h<0: return (0,0,0,0)
  return (x, y, w, h)  

def isEmpty(a):
   return a == (0,0,0,0) 

def isIntersect(a, b):
    return not isEmpty(intersection(a,b))

