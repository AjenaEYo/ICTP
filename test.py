import numpy as np
from PIL import ImageFont,ImageDraw,Image
import cv2 as cv


font = ImageFont.truetype("fonts/gulim.ttc",20)

img = np.full((200,300,3),(255,255,255),np.uint8)

img = Image.fromarray(img)

draw= ImageDraw.Draw(img)

text = "한글은"

draw.text((30,50),text,font=font,fill=(0,0,0))

img = np.array(img)

cv.imshow("text",img)

cv.waitKey()

cv.destroyAllWindows()