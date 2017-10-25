from mask import *

bound =[([160, 30, 30], [179, 200, 200], [0, 0, 0]), 
       ([0, 30, 30], [22, 150, 150], [1, 0, 0]), 
       ([22, 30, 30], [38, 150, 150], [2, 0, 0]), 
       ([38, 30, 30], [75, 150, 150], [3, 0, 0]), 
       ([75, 30, 30], [130, 150, 150], [4, 0, 0]),  
       ([130, 30, 30], [160, 150, 150], [5, 0, 0]), 
       ([0, 0, 0], [160, 10, 10], [7, 0, 0]), 
       ([0, 200, 200], [160, 255, 255], [8, 0, 0]) 
       ] 

def color(c):
    if c == 0: return "red"
    elif c == 1: return "beige"
    elif c == 2: return "yellow"
    elif c == 3: return "green"
    elif c == 5: return "violet"
    elif c == 4: return "blue"
    elif c == 6: return "pink"
    elif c == 8: return "white"
    elif c == 7: return "black"

def color_detection(windows,image):
    height, width, channels = image.shape
    building_coordinates = (0,0,width, height)
    c_mask = get_mask(windows, building_coordinates, image)
    output = cv2.bitwise_and(image, image, mask=c_mask)
    hsv_img = cv2.cvtColor(output, cv2.COLOR_BGR2HSV)
    all_colors = np.zeros(9)
    for (lower, upper, c) in bound:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        mask = cv2.inRange(hsv_img, lower, upper)
        total_mask = np.logical_and(c_mask, mask)
        pix = np.count_nonzero(total_mask)
        all_colors[c[0]] += pix
    max = np.amax(all_colors)
    indx = np.where(all_colors == max)[0]
    building_color = color(indx)
    return building_color










