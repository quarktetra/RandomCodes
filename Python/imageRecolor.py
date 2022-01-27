## @knitr imageRecolorpy
# Replacing a target color in an image with another one
# 09/30/2021, tetraquark@gmail.com
# https://tetraquark.netlify.app/post/pythonRecolor/index.html

from PIL import Image
import math
imgName=   'C:/Users/451516/Documents/github/tetraquark_c_tester/content/post/energyflow/spr.png'
img = Image.open(imgName)

pixels = img.load()
targetColor=[255,255,255]   # the original color
replacementColor=(245,244,241)    # replacement color
#replacementColor=(255,0,0)
offsetSquared=100  # this is the sum of the squares of RGB values. Set this to 0 if you want the exact RGB value

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if (pixels[i, j][0]-targetColor[0])**2 +(pixels[i, j][1]-targetColor[1])**2 +(pixels[i, j][2]-targetColor[1])**2 < offsetSquared:
         pixels[i, j] = replacementColor

#img.show()
imgNameS=imgName.split(".")
img.save(imgNameS[0]+"_recolored."+imgNameS[1] )



