## @knitr imageRecolorLooppy
# Replacing a target color in an image with another one
# 09/30/2021, tetraquark@gmail.com
# https://tetraquark.netlify.app/post/pythonRecolor/index.html

from PIL import Image
import math
import glob, os
#print (os.getcwd())

addTag="R"  # add a text here if you don't want to overwrite the original images
addTag=""
#path ='C:/Users/451516/Documents/github/CaltechLigoOpticalShutterN/_book/'


path ='C:/Users/451516/Documents/github/CaltechLigoCircuits/figure/'
path ='C:/Users/451516/Documents/github/CaltechLigoCircuits/figure/'
#path ='C:/Users/451516/Documents/github/CaltechLigoCircuits/imgFolder/'
pathT ='C:/Users/451516/Documents/github/CaltechLigoCircuits/_book/'
path ='C:/Users/451516/Documents/github/aLIGOrfPhotoDetectors/'
pathT ='C:/Users/451516/Documents/github/aLIGOrfPhotoDetectors/'


#path ='C:/Users/451516/Documents/github/CaltechLigoOpticalShutterN/_book/CaltechLigoOpticalShutterN_files/figure-revealjs/'

path ='C:/Users/451516/Documents/github/tetraquark_c/content/post/conformalmap/index_files/figure-html/'
pathT ='C:/Users/451516/Documents/github/tetraquark_c/content/post/conformalmap/index_files/figure-html/'

print(path )
imgNames = [f for f in os.listdir(path) if f.endswith('.png') ]    #or f.endswith('.jpg')
#imgNames=['invninvj-1.png']

#imgNames=['outlineModel.png']
if 0:
    imgNames=["jfampstacked-1.png"]
    imgNames=  [ 'conceptRs2.png' ]
    imgNames=['ampNoiseOnly-1.png']
    imgNames=['NinvAmpNoiseOnly-1.png','invAmpNoiseOnly-1.png']
    imgNames=['coax-1.png']
    imgNames=['flicker.png']
    
    imgNames=['jfModelflat-1.png' ]
    imgNames=['invninvj-1.png','NinvAmpNoiseOnly-1.png','invAmpNoiseOnly-1.png']
    
    imgNames=['LTspiceNoninvertingOpampNoiseLT1001.png']
    imgNames=['LTspiceNoninvertingOpampNoiseLT1001shortRin.png','LTspiceNoninvertingOpampNoiseLT1001.png']
    imgNames=['non_inverting_op_amp_noise_LT1001_shortRin_unit_gain.png','non_inverting_op_amp_noise_LT1001_5Krin_unit_gain.png','non_inverting_op_amp_noise_LT1001_1MEGArin_unit_gain.png']
    
    imgNames=['low_noise_4_fet_preampM.png']
    imgNames=['preampSingleEnded.png']
    imgNames=['kealPPT.png']



print(imgNames )



for imgName in imgNames:
    print("working on:"+ imgName )
    img = Image.open( path+imgName)
    img = img.convert("RGBA")



    pixels = img.load()
    targetColor=[255,255,255]   # the original color
   # targetColor=[192,192,192]   # the original color

    replacementColor=(0,0,0,0)# (245,244,241,0)    # replacement color
    offsetSquared=5  # this is the sum of the squares of RGB values. Set this to 0 if you want the exact RGB value

    for i in range(img.size[0]):
        for j in range(img.size[1]):

           if (pixels[i, j][0]-targetColor[0])**2 +(pixels[i, j][1]-targetColor[1])**2 +(pixels[i, j][2]-targetColor[2])**2 < offsetSquared:
                 pixels[i, j] = replacementColor
    #img.show()
    imgNameSp=imgName.split(".")
    img.save(pathT+imgNameSp[0]+addTag+"."+imgNameSp[1])
    print("saved:"+imgNameSp[0]+addTag+"."+imgNameSp[1])
print('done')



