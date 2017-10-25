import argparse
import cv2, glob

result = open("bg.txt", "w+")

for imagePath in glob.glob("neg" + "/*"):
    result.write(imagePath + "\n")
