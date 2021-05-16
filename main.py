import cv2 as cv
import numpy as np
import os
from time import time
import easyocr
from google_trans_new import google_translator
from module.WindowCapture import WindowCapture
from module.Vision import Vision

from PIL import ImageFont, ImageDraw, Image


# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def draw_text(image, bounds,color = 'yellow',width=2):
    img = Image.fromarray(image)
    draw = ImageDraw.Draw(img)
    font=ImageFont.truetype("fonts/gulim.ttc",20)
    for bound  in bounds:
        (top_left, top_right, bottom_right, bottom_left)=bound[0]
        text = bound[1];
        top_left = (int(top_left[0]), int(top_left[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
        draw.text(top_left,text,font=font,fill=(0,0,0))
        #cv.rectangle(img=image, pt1=top_left, pt2=bottom_right, color=(255, 0, 0), thickness=10)

def draw_box(image, bounds,color = 'yellow',width=2):
    for bound  in bounds:
        (top_left, top_right, bottom_right, bottom_left)=bound[0]
        text = bound[1];
        top_left = (int(top_left[0]), int(top_left[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

        cv.rectangle(img=image, pt1=top_left, pt2=bottom_right, color=(255, 0, 0), thickness=10)
        #cv.putText(image, text, (top_left[0], bottom_left[1] - 10),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        

    
# initialize the WindowCapture class
wincap = WindowCapture('1234.mkv - 팟플레이어')
# initialize the Vision class
#vision_limestone = Vision('albion_limestone.jpg')

'''
# https://www.crazygames.com/game/guns-and-bottle
wincap = WindowCapture()
vision_gunsnbottle = Vision('gunsnbottle.jpg')
'''
reader = easyocr.Reader(['en']);

translator = google_translator()
#translate_text = translator.translate('I am GROOT',lang_src='en',lang_tgt='ko')
#print(translate_text)
loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    #points = vision_limestone.find(screenshot, 0.5, 'rectangles')
    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')
    bounds = reader.readtext(screenshot, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch', blocklist='=-')  #Reading with bounds
    bounds_ko = []
    #print(bounds)
    for bound  in bounds:
        text = bound[1]
        text_ko = translator.translate(text,lang_tgt='ko',lang_src='en')
        y = list(bound)
        y[1] = text_ko
        bounds_ko.append(tuple(y))
 
    draw_box(screenshot,bounds_ko)
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