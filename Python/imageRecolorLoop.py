## @knitr imageRecolorLooppy
# Replacing a target color in an image with another one
# 09/30/2021, tetraquark@gmail.com
# https://tetraquark.netlify.app/post/pythonRecolor/index.html

from PIL import Image
import math
import glob, os
#print (os.getcwd())

addTag=""  # add a text here if you don't want to overwrite the original images
path =os.getcwd()
print(path )
imgNames = [f for f in os.listdir(path) if f.endswith('.png') or f.endswith('.jpg')]
print(imgNames )

for imgName in imgNames:
    img = Image.open(imgName)
    img = img.convert("RGBA")



    pixels = img.load()
    targetColor=[255,255,255]   # the original color
    #replacementColor=(245,244,241)    # replacement color
    replacementColor=(245,244,241,0)    # replacement color
    offsetSquared=12  # this is the sum of the squares of RGB values. Set this to 0 if you want the exact RGB value

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if (pixels[i, j][0]-targetColor[0])**2 +(pixels[i, j][1]-targetColor[1])**2 +(pixels[i, j][2]-targetColor[1])**2 < offsetSquared:
             pixels[i, j] = replacementColor

    #img.show()
    imgNameSp=imgName.split(".")
    img.save(imgNameSp[0]+addTag+"."+imgNameSp[1])




