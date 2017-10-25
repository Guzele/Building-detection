import numpy as np
import cv2

def get_mask(win_c,bld_c,img):
    bld = np.array(bld_c, dtype="uint16")
    win = np.array(win_c, dtype="uint16")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = np.zeros_like(gray)
    p = bld
    x1,y1 = p[0],p[1]
    x2,y2 = p[0] + p[2],p[1]+ p[3]
    mask[y1:y2, x1:x2] = 255
    for w in win:
        x1, y1 = w[0], w[1]
        x2 = w[0] + w[2]
        y2 = w[1] + w[3]
        mask[y1:y2, x1:x2] = 0
    return mask
