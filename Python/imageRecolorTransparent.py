## @knitr imageRecolorpy
## @knitr imageRecolorpy
# Replacing a target color in an image with another one
# 09/30/2021, tetraquark@gmail.com
# https://tetraquark.netlify.app/post/pythonRecolor/index.html

from PIL import Image
import math
imgName=   'C:/Users/451516/Documents/github/aLIGOrfPhotoDetectors/vout9_1MHZ_ext.png'
imgName='C:/Users/451516/Documents/github/tetraquark_c/content/post/rlcfilters/filters.png'
imgName='C:/Users/451516/Documents/github/tetraquark_c/public/post/rlcfilters/9_1MHzBP_freq_response.png'
imgName='C:/Users/451516/Documents/github/tetraquark_c/public/post/ligomodulation/PDH.png'
imgName='C:/Users/451516/Documents/github/tetraquark_c/content/post/ligomodulation/PDH.png'
imgName=   'C:/Users/451516/Documents/github/aLIGOrfPhotoDetectors/PDH.png'
imgName='C:/Users/451516/Documents/github/tetraquark_c/content/post/ligomodulation/transvers_E-O_phase_mod_800w.png'
imgName='C:/Users/451516/Documents/github/tetraquark_c/content/post/quantum_hosc_coherent/oscillator.png'
imgName='C:/Users/451516/Documents/github/Explorer/pLOGO.png'
imgName='C:/Users/451516/Documents/github/Explorer/roadmap.png'
imgName='C:/Users/451516/Documents/github/tetraquark_cbeta/content/post/sbgw/param.png'

imgName='C:/Users/451516/Documents/github/tetraquark_cbeta/content/post/sbgw/KinkCuspSL.png'
imgName='C:/Users/451516/Documents/github/tetraquark_cbeta/content/post/sbgw/KinkCuspLL.png'

imgName='C:/Users/451516/Documents/github/tetraquark_cbeta/content/post/ligo_snr_reopt/filterAlgo.png'

img = Image.open(imgName)
img = img.convert("RGBA")

pixels = img.load()
targetColor=[255,255,255]   # the original color
#targetColor=[0,0,0]   # the original color
#targetColor=[192,192,192]   # the original color   LTspice
replacementColor=(245,244,241,0)    # replacement color
#replacementColor=(255,255,255,0)    # replacement color

#replacementColor=(0,0,0,0)    # replacement color
#replacementColor=(255,0,0)
offsetSquared=100  # this is the sum of the squares of RGB values. Set this to 0 if you want the exact RGB value

for i in range(img.size[0]):
    for j in range(img.size[1]):
        if (pixels[i, j][0]-targetColor[0])**2 +(pixels[i, j][1]-targetColor[1])**2 +(pixels[i, j][2]-targetColor[1])**2 < offsetSquared:
         pixels[i, j] = replacementColor

#img.show()
imgNameS=imgName.split(".")
img.save(imgNameS[0]+"."+imgNameS[1] )



