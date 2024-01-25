## @knitr imageRecolorLooppy
# Replacing a target color in an image with another one
# 09/30/2021, tetraquark@gmail.com
# https://tetraquark.netlify.app/post/pythonRecolor/index.html

from PIL import Image
import math
import glob, os
#print (os.getcwd())

addTag=""  # add a text here if you don't want to overwrite the original images
#path ='C:/Users/451516/Documents/github/CaltechLigoOpticalShutterN/_book/'


path ='C:/Users/451516/Documents/github/CaltechLigoCircuits/figure/'
path ='C:/Users/451516/Documents/github/CaltechLigoCircuits/figure/'
path ='C:/Users/451516/Documents/github/CaltechLigoCircuits/imgFolder/'
pathT ='C:/Users/451516/Documents/github/CaltechLigoCircuits/_book/'
#path ='C:/Users/451516/Documents/github/CaltechLigoOpticalShutterN/_book/CaltechLigoOpticalShutterN_files/figure-revealjs/'

print(path )
imgNames = [f for f in os.listdir(path) if f.endswith('.png') ]    #or f.endswith('.jpg')
imgNames=['collection.png']
print(imgNames )

for imgName in imgNames:
    print(imgName )
    img = Image.open( path+imgName)
    img = img.convert("RGBA")



    pixels = img.load()
    targetColor=[17,40,74]   # the original color
    targetColor2=[36,97,160]  # the original color
    targetColor3=[45,107,164]  # the original color
    targetColor4=[15,38,72]  # the original color
    targetColor5=[39,35,50]  # the original color

    replacementColor=(0,0,0,0)# (245,244,241,0)    # replacement color
    offsetSquared=1000  # this is the sum of the squares of RGB values. Set this to 0 if you want the exact RGB value

    for i in range(img.size[0]):
        for j in range(img.size[1]):

           if (pixels[i, j][0])**2 +(pixels[i, j][1])**2 +5000 < (pixels[i, j][2])**2:
                 pixels[i, j] = replacementColor
           if (pixels[i, j][0]-targetColor[0])**2 +(pixels[i, j][1]-targetColor[1])**2 +(pixels[i, j][2]-targetColor[2])**2 < offsetSquared:
                 pixels[i, j] = replacementColor
    #img.show()
    imgNameSp=imgName.split(".")
    img.save(pathT+imgNameSp[0]+addTag+"."+imgNameSp[1])

print('done')


