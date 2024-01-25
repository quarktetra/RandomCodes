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
path ='C:/Users/451516/Documents/github/CaltechLigoCircuits/imgFolder/'
path ='C:/Users/451516/Documents/github/aLIGOrfPhotoDetectors/img/'

#path ='C:/Users/451516/Documents/github/CaltechLigoOpticalShutterN/_book/CaltechLigoOpticalShutterN_files/figure-revealjs/'

print(path )
imgNames = [f for f in os.listdir(path) if f.endswith('.png') ]    #or f.endswith('.jpg')
#imgNames=  [ 'conceptR.png' ]
print(imgNames )

maskcoord1=[145,415]
maskcoord2=[797,621]

Lmaskcoord1=[1891,245]
Lmaskcoord2=[1993,679]
for imgName in imgNames:
    print(imgName )
    img = Image.open( path+imgName)
    img = img.convert("RGBA")



    pixels = img.load()
    targetColor=[192,192,192]   # the original color   LTspice
    targetColor2=[192,192,192]   # the original color
    targetColor3=[192,192,192]    # the original color
    #replacementColor=(245,244,241)    # replacement color
    replacementColor=(0,0,0,0)#(245,244,241,0)    # replacement color
    offsetSquared=3000  # this is the sum of the squares of RGB values. Set this to 0 if you want the exact RGB value

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if 0 and ((maskcoord1[0]<i<maskcoord2[0] ) and (maskcoord1[1]<j<maskcoord2[1] ) or (Lmaskcoord1[0]<i<Lmaskcoord2[0] ) and (Lmaskcoord1[1]<j<Lmaskcoord2[1] )):
                pass
            else:
                if (pixels[i, j][0]-targetColor[0])**2 +(pixels[i, j][1]-targetColor[1])**2 +(pixels[i, j][2]-targetColor[2])**2 < offsetSquared:
                 pixels[i, j] = replacementColor
                if (pixels[i, j][0]-targetColor2[0])**2 +(pixels[i, j][1]-targetColor2[1])**2 +(pixels[i, j][2]-targetColor2[2])**2 < offsetSquared:
                 pixels[i, j] = replacementColor
                if (pixels[i, j][0]-targetColor3[0])**2 +(pixels[i, j][1]-targetColor3[1])**2 +(pixels[i, j][2]-targetColor3[2])**2 < offsetSquared:
                 pixels[i, j] = replacementColor


    #img.show()
    imgNameSp=imgName.split(".")
    img.save(path+imgNameSp[0]+addTag+"."+imgNameSp[1])




