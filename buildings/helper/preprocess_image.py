import argparse
import cv2, glob

def preprocess(imageName):
   image =  cv2.imread(imageName)
   #image = cv2.resize(image,(600, 600))

   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

   #histogram equalization, for different light conditions
   image_histogram = cv2.equalizeHist(gray)

   #cv2.imshow("Original", gray)
   #cv2.imshow("With histogram", image_histogram)
   #cv2.waitKey(0)
   return image_histogram
   #preprocess('facade_0_0053403_0053679.png')

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required=True,
                 help="path to the input folder\n replaces all images(files) with filtered ones!")
args = vars(ap.parse_args())
for imagePath in glob.glob(args["folder"] + "/*"):
    #print imagePath
    output = preprocess(imagePath)
    cv2.imwrite(imagePath, output)


