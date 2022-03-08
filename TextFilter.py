import pyautogui
from PIL import Image
import time
import math

#insert picture path here
image = Image.open(r"Path")
pix = image.load()

Result = ""
Brightness = 0
Enterpress = 0
i = 0
Sybols = ["@", "#", "§", "?", "!", "+", "*","-", "."]

time.sleep(3)

for y in range(200):
    for x in range(200):
        r = pix[x,y][0]
        g = pix[x,y][1]
        b = pix[x,y][2]
        pix[x,y] = (r, g, b)
        Brightness = (r+g+b) / 3
        Result = Result + Sybols[math.ceil(Brightness/36)]
        Enterpress += 1

        if Enterpress >= 200:
            print(Result)
            Result = ""
            Enterpress = 0