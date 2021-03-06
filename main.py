import cv2 as cv
import numpy as np
import os
from time import time
import easyocr
from module.WindowCapture import WindowCapture
from kakaotrans import Translator

from PIL import ImageFont, ImageDraw, Image
import module.selectWindow as selectWindow

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def draw_text(image, bounds,color = 'yellow',width=2):
    img = Image.fromarray(image)
    draw = ImageDraw.Draw(img)
    font=ImageFont.truetype("fonts/gulim.ttc",15)
    for bound  in bounds:
        (top_left, top_right, bottom_right, bottom_left)=bound[0]
        text = bound[1];
        top_left = (int(top_left[0]), int(top_left[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
        size = font.getsize(text)
        fontimg = Image.new('RGB', size=size, color=(0, 0, 0))
        fontdraw = ImageDraw.Draw(fontimg)
        fontdraw.text((0, 0), text, fill=(209, 239, 8), font=font)
        img.paste(fontimg,top_left)
        # draw.rectangle((top_left[0], top_left[1], bottom_right[0], bottom_right + h), fill='black')
        # draw.text(top_left,text,font=font,fill=(255,255,255))
    
    image=np.array(img)
    return image

        #cv.rectangle(img=image, pt1=top_left, pt2=bottom_right, color=(255, 0, 0), thickness=10)

def draw_box(image, bounds,color = 'yellow',width=2):
    for bound  in bounds:
        (top_left, top_right, bottom_right, bottom_left)=bound[0]
        text = bound[1];
        top_left = (int(top_left[0]), int(top_left[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

        cv.rectangle(img=image, pt1=top_left, pt2=bottom_right, color=(0, 255, 255), thickness=1)
        #cv.putText(image, text, (top_left[0], bottom_left[1] - 10),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        

    
# initialize the WindowCapture class

selectWindow.on()

hwnd = selectWindow.prehwnd

wincap = WindowCapture(hwnd)
# initialize the Vision class
#vision_limestone = Vision('albion_limestone.jpg')

'''
# https://www.crazygames.com/game/guns-and-bottle
wincap = WindowCapture()
vision_gunsnbottle = Vision('gunsnbottle.jpg')
'''
reader = easyocr.Reader(['en']);
translator= Translator()

loop_time = time()
cv.namedWindow('Computer Vision', cv.WINDOW_NORMAL)
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

   
    # debug the loop rate
    fps='FPS {}'.format(1 / (time() - loop_time))
    print(fps)
    loop_time = time()
    cv.putText(screenshot, fps, (0, 10),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv.imshow('Computer Vision', screenshot)
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    # if cv.waitKey(1) == ord('q'):
    #     cv.destroyAllWindows()
    #     break
    k = cv.waitKey(1)
    if k == ord('q'): # esc key
        cv.destroyAllWindows()
        break
    elif k == ord('t'): # 's' key
        loop_time = time()
        #bounds = reader.readtext(screenshot, add_margin=0.55, width_ths=0.7, link_threshold=0.8, decoder='beamsearch', blocklist='=-')  #Reading with bounds
        bounds = reader.readtext(screenshot)
        bounds_ko = []
        #print(bounds)
        for bound  in bounds:
            text = bound[1]
            text_ko = translator.translate(text,src='en',tgt='kr')
            y = list(bound)
            y[1] = text_ko
            bounds_ko.append(tuple(y))
        
        draw_box(screenshot,bounds_ko)
        screenshot=draw_text(screenshot,bounds_ko)
        fps='FPS {}'.format(1 / (time() - loop_time))
        cv.putText(screenshot, fps, (0, 10),cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv.imshow('Computer Vision', screenshot)
        cv.waitKey(0)
        

print('Done.')