import argparse
from os import listdir

from detector import detectAll

def check(train_dir):
   direct = 'buildings/'+ train_dir
   files = sorted(listdir(direct))
   for train_file in files:
       full_name  = direct + '/' + train_file
       print full_name
       detectAll(full_name)
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default = "",
	help="path to the input image")
args = vars(ap.parse_args())

imageName = args["image"]
if imageName != '':
     detectAll(imageName)
else:
     check('additional/pos')
     check('additional/neg')
     check ('lol')
     check ('show')#check('pos/test')
