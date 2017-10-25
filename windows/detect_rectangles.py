import cv2
import numpy as np

def bound(color):
    if color == "red": return [0,0,255]
    elif color == "blue": return [255,85,0]
    elif color == "white": return [255,255,255]

def detectRect(imageName, color):
    image = cv2.imread(imageName)
    b = bound(color)
    boundaries = np.array(b, dtype="uint8")
    mask = cv2.inRange(image, boundaries, boundaries)
    output = cv2.bitwise_and(image, image, mask=mask)
    #cv2.imshow("output",output)
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 50, 250, cv2.THRESH_BINARY)[1]
    #cv2.imshow("dv",thresh)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                           cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0]
    #cv2.waitKey()
    rect_coordinates = []
    
    for c in cnts:
        rect = cv2.boundingRect(c)

        x, y, w, h = rect 
        '''h = 4
        w = 4
        rect = (x, y, w, h)'''
        if h < 4 or w < 4:
             continue
        '''if h > w:
           w = h
        else:
           h = w'''
        #crop_img = image[y: y + h, x: x + w] # Crop from x, y, w, h -> 100, 200, 300, 400
        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
        #cv2.imshow("cropped", crop_img)
        #cv2.waitKey(0)

        rect_coordinates.append(rect)
    return rect_coordinates

