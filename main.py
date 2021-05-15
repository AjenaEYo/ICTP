import cv2 as cv
import numpy as np
import os
from time import time

from module.WindowCapture import WindowCapture
from module.Vision import Vision

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture('팟플레이어')
# initialize the Vision class
#vision_limestone = Vision('albion_limestone.jpg')

'''
# https://www.crazygames.com/game/guns-and-bottle
wincap = WindowCapture()
vision_gunsnbottle = Vision('gunsnbottle.jpg')
'''

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    #points = vision_limestone.find(screenshot, 0.5, 'rectangles')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')
    cv.imshow('Computer Vision', screenshot)
    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')