import Image

path ='C:/Users/451516/Documents/github/CaltechLigoOpticalShutterN/_book/'

imgName='10.jpg'

im = Image.open(path+imgName)



im.save("file.jpg", "JPEG")

im1 = Image.open(path+imgName)
im1.save(r'path where the PNG will be stored\new file name.png')