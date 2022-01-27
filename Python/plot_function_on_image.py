## @knitr imagepy
# Fitting a voltage curve on plot image
#  12/29/2021, tetraquark@gmail.com
# https://tetraquark.netlify.app/post/energyflow/#Turtlesallthewayupanddown

from PIL import Image, ImageDraw
import math
import matplotlib.pyplot as plt
import numpy as np
imgPath=""
imgid= 'events.png' # taken from https://docs.google.com/presentation/d/1onHMsDkEARxagluUmHHS2as6YPWWAyDO/edit?rtpof=true&sd=true

img = Image.open(imgPath+imgid)

pixels = img.load()
#calibrate these values to match the origin, xrange and aspect ratio
cx=110
cy=img.size[1]-705

xrange= img.size[0]
aspectR=0.895


def calib(x):
    tv=x -cx
    vv=   img.size[1]-tv*aspectR   -cy
    return  vv

def drawC(draw,scaleCircle,colorIn):
    leftUpPoint = (scaleCircle[0]-scaleCircle[2], scaleCircle[1]-scaleCircle[2])
    rightDownPoint = (scaleCircle[0]+scaleCircle[2], scaleCircle[1]+scaleCircle[2])
    draw.ellipse([leftUpPoint, rightDownPoint],  outline =colorIn)

for i in range(cx,xrange):
    for j in range(3):
            h=  calib(i)+j
            if 1<h< img.size[1]:
             pixels[i,h ] = (0, 0,255)

#draw = ImageDraw.Draw(img)
#draw.ellipse((20, 20, 180, 180), fill=(255, 0, 0),  outline ='blue')

draw = ImageDraw.Draw(img)
scaleCircles = [[666,651,38,1000],[666,569,26,100],[666,487,14,10],[666,406,2.5,1]]
sOccurance=[]
sOccuranceLF=[]
sOccuranceL=[]
sRadius=[]
sRadiusF=[]
for scaleCircle in scaleCircles:
    drawC(draw,scaleCircle,'red')
    sOccurance.append(scaleCircle[3])
    sOccuranceL.append(math.log10(scaleCircle[3]) )
    sRadius.append(scaleCircle[2])

# fit a line to scales to find the mapping
m, b = np.polyfit(sOccuranceL,sRadius , 1)


for sOcc in sOccuranceL:
      sRadiusF.append(   sOcc*m+b   )



if False:
    #plt.plot(nNodes, oneRadii, label='oneRadii')
   # plt.plot(nNodesL, oneRadii, label='oneRadii vs nodesL')
    plt.plot(sOccuranceL,sRadius, label='sOccuranceL vs sRadius')
    plt.plot(sOccuranceL,sRadiusF, label='sOccuranceL vs sRadius Fit')
   # plt.plot(sOccuranceLF,sRadius, label='sOccuranceL fit vs sRadius')

    plt.xlabel('sOccurance Log')
    plt.ylabel('occurences Radius')
    plt.title('Scale circles')
    plt.show()

oneCircles = [[139,681,65,1],[139,607,49,2],[139,564,42,3],[139,534,37,4],[139,510,33,5],[139,492,30,6],[139,475,28,7],[139,461,27,8]] #,[139,370,19,20]
nNodes=[]
nNodesL=[]
oneRadiiL=[]
logEvents=[]
oneRadii=[]
RadNormalizer=oneCircles[0][2]
for Circle in oneCircles:
    nNodes.append(Circle[3] )
    nNodesL.append(math.log10(Circle[3] )  )

    #drawC(draw,Circle,'blue')
    oneRadii.append(Circle[2])
    oneRadiiL.append(math.log10(Circle[2] ))
    logEvents.append( (Circle[2]-b)/m)


    #draw.ellipse((20, 20, 180, 180), fill=(255, 255, 0),  outline ='blue')


#img.show()




mE, bE = np.polyfit(nNodesL,logEvents , 1)

logEventsF=[]
for nNondeL in nNodesL:
      logEventsF.append(   nNondeL*mE+bE   )


mNL, bNL = np.polyfit(nNodesL,oneRadiiL, 1)

oneRadiiLF=[]
oneRadiiF=[]
for this in nNodesL:
      oneRadiiLF.append(   this*mNL+bNL   )
      oneRadiiF.append(  10** (this*mNL+bNL)   )



if False:
    #plt.plot(nNodes, oneRadii, label='oneRadii')
   # plt.plot(nNodesL, oneRadii, label='oneRadii vs nodesL')
    #plt.plot(nNodesL, oneRadiiL, label='oneRadiiL vs nodesL')
   # plt.plot(nNodes, oneRadiiL, label='oneRadiiL vs nodesL')
    plt.plot(nNodes, oneRadii, label='oneRadii vs nodes')
    plt.plot(nNodes, oneRadiiF, label='oneRadii fit vs nodes')
    #plt.plot(nNodesL, logEvents, label='x:nodesL vs y:logEvents')
    #plt.plot(nNodesL, logEventsF, label='x:nodesL vs y:logEvents Fit')
    #plt.plot(nNodes, logEvents, label='x:nodes vs y:logEvents')

    plt.xlabel('number of nodes aaffected')
    #plt.ylabel('occurences Radius')
    plt.title('Number of racks affected=1 x:nodes vs y:')
    plt.show()
#oneCircles = [[139,681,65,1],[139,607,49,2],[139,564,42,3],[139,534,37,4],[139,510,33,5],[139,492,30,6],[139,475,28,7],[139,461,27,8]] #,[139,370,19,20]

def yloc(theindex):
    y1=681;y2=607; delta=y1-y2
    yval=y1-math.log10(theindex)*delta /math.log10(2)
    return yval


def xloc(theindex):
    x1=139;x2=221; delta=x2-x1
    xval=x1+math.log10(theindex)*delta /math.log10(2)
    return xval
diagCircles=[]
thisi=1
diagCircles.append([xloc(thisi),yloc(thisi),65,thisi])
thisi=2
diagCircles.append([xloc(thisi),yloc(thisi),51,thisi])
thisi=3
diagCircles.append([xloc(thisi),yloc(thisi),38,thisi])

thisi=4
diagCircles.append([xloc(thisi),yloc(thisi),30,thisi])

thisi=5
diagCircles.append([xloc(thisi),yloc(thisi),24,thisi])

thisi=6
diagCircles.append([xloc(thisi),yloc(thisi)+1,21,thisi])


thisi=7
diagCircles.append([xloc(thisi),yloc(thisi)+1,19,thisi])


thisi=8
diagCircles.append([xloc(thisi)-2,yloc(thisi)+2,17,thisi])

thisi=9
diagCircles.append([xloc(thisi)-2,yloc(thisi)+2,16,thisi])

thisi=10
diagCircles.append([xloc(thisi)-2,yloc(thisi)+2,15,thisi])

nmax=20
thisi=nmax
diagCircles.append([xloc(thisi)-2,yloc(thisi)+2,14,thisi])




#diagCircles = [[139,681,65,1],[221,607,51,2],[269,565,38,3],[269,565,38,4]]        #,[368,475,20,7],[440,410,11,12]
dNodesL=[]
dRadiiL=[]

dNodes=[]
dNodesI=[]
dRadii=[]
dEvents=[]

for Circle in diagCircles:
   #drawC(draw,Circle,'red')
   dNodes.append(Circle[3])
   dNodesI.append(math.log(math.factorial(Circle[3])) )
   dNodesL.append(math.log10(Circle[3]) )
   dRadii.append(Circle[2])
   dRadiiL.append(math.log10(Circle[2]) )
   dEvents.append(   10**((Circle[2]-b)/m )  )

diag_mL, diag_bL = np.polyfit(dNodesL,dRadiiL, 1)
diag_q,diag_m, diag_b = np.polyfit(dNodes,dRadiiL, 2)

dRadiiLF=[]
dRadiiLF2=[]
dRadiiF=[]
for this in dNodes:
      dRadiiLF.append(   this*this*diag_q+this*diag_m+diag_b  )
      #dRadiiLF2.append(   math.log10(this)*diag_mL+diag_bL  )
      #dRadiiF2.append(  10** (this*diag_mL+diag_bL)   )

if False:
    #plt.plot(nNodes, oneRadii, label='oneRadii')
   # plt.plot(nNodesL, oneRadii, label='oneRadii vs nodesL')
    #plt.plot(nNodesL, oneRadiiL, label='oneRadiiL vs nodesL')
   # plt.plot(nNodes, oneRadiiL, label='oneRadiiL vs nodesL')
    #plt.plot(dNodes, dRadiiLF2, label='Fit ')
    plt.plot(dNodes, dRadii, label='manual', marker='x')
    #plt.plot(dNodes, dRadiiLF, label='fit')
    #plt.plot(dNodesL, dRadiiF, label='dRadii F vs dnodes')
    #plt.plot(nNodes, oneRadiiF, label='oneRadii fit vs nodes')
    #plt.plot(nNodesL, logEvents, label='x:nodesL vs y:logEvents')
    #plt.plot(nNodesL, logEventsF, label='x:nodesL vs y:logEvents Fit')
    #plt.plot(nNodes, logEvents, label='x:nodes vs y:logEvents')

    plt.xlabel('number of nodes aaffected')
    plt.legend()
    #plt.ylabel('occurences Radius')
    plt.title('Number of racks affected=i x:nodes vs y:')
    #plt.show()

fourCircles=[]
thisi=4
fourCircles.append([xloc(4),yloc(thisi)+2,30,thisi])
thisi=5
fourCircles.append([xloc(4),yloc(thisi)+2,24,thisi])
thisi=6
fourCircles.append([xloc(4),yloc(thisi)+2,17,thisi])
thisi=7
fourCircles.append([xloc(4),yloc(thisi)+2,12,thisi])

fourNodesL=[]
fourRadiiL=[]

fourNodes=[]
fourRadii=[]
fourEvents=[]
for Circle in fourCircles:
    #drawC(draw,Circle,'orange')
    fourNodes.append(Circle[3])
    fourNodesL.append(math.log10(Circle[3]) )
    fourRadii.append(Circle[2])
    fourRadiiL.append(math.log10(Circle[2]) )
    fourEvents.append(   10**((Circle[2]-b)/m )  )

four_mL, four_bL = np.polyfit(fourNodesL,fourRadiiL, 1)

fourRadiiLF=[]
fourRadiiF=[]
fourEventsF=[]
for this in fourNodesL:
      fourRadiiLF.append(   this*four_mL+four_bL   )
      fourRadiiF.append(  10** (this*four_mL+four_bL)   )
      thisN=10**this
      thisR=10**(this*four_mL+four_bL)
      fourEventsF.append(   10**((thisR-b)/m )  )
if False:
    plt.plot(fourNodes,fourEvents, label='Manually adjusted', marker='x')
    plt.plot(fourNodes, fourEventsF, label='Logarithmic Fit')


    plt.xlabel('number of nodes affected')
    plt.ylabel('occurences')
    plt.title('Number of racks affected=4')
    plt.yscale("log")
    plt.legend()
    plt.grid(color='gray', linestyle='-', linewidth=0.5)
    txt="Figure 7: # of nodes affected vs # of occurences ."
    plt.figtext(0.5, -0.09, txt, wrap=True, horizontalalignment='center', fontsize=14);
    #plt.show()


fourCircles=[]
thisi=5
fourCircles.append([xloc(5),yloc(thisi)+2,25,thisi])
thisi=6
fourCircles.append([xloc(5),yloc(thisi)+2,18,thisi])
thisi=7
fourCircles.append([xloc(5),yloc(thisi)+2,15,thisi])
thisi=8
fourCircles.append([xloc(5),yloc(thisi)+2,11,thisi])

fourNodesL=[]
fourRadiiL=[]

fourNodes=[]
fourRadii=[]
fourEvents=[]
for Circle in fourCircles:
    drawC(draw,Circle,'green')
    fourNodes.append(Circle[3])
    fourNodesL.append(math.log10(Circle[3]) )
    fourRadii.append(Circle[2])
    fourRadiiL.append(math.log10(Circle[2]) )
    fourEvents.append(   10**((Circle[2]-b)/m )  )
four_mL, four_bL = np.polyfit(fourNodesL,fourRadiiL, 1)

fourRadiiLF=[]
fourRadiiF=[]
fourEventsF=[]
for this in fourNodesL:
      fourRadiiLF.append(   this*four_mL+four_bL   )
      fourRadiiF.append(  10** (this*four_mL+four_bL)   )
      thisN=10**this
      thisR=10**(this*four_mL+four_bL)
      fourEventsF.append(   10**((thisR-b)/m )  )

print(four_mL, four_bL)
plt.plot(fourNodes,fourEvents, label='Manually adjusted', marker='x')
plt.plot(fourNodes, fourEventsF, label='Logarithmic Fit')


plt.xlabel('number of nodes affected')
plt.ylabel('occurences')
plt.title('Number of racks affected=4')
plt.yscale("log")
plt.legend()
plt.grid(color='gray', linestyle='-', linewidth=0.5)
txt="Figure 7: # of nodes affected vs # of occurences ."
plt.figtext(0.5, -0.09, txt, wrap=True, horizontalalignment='center', fontsize=14);
#plt.show()




twoCircles = [[221,607,51,2],[221,564,42,3],[221,534,36,4],[221,511,33,5],[221,491,30,6],[221,475,28,7]]   #,[221,461,26,7],[221,370,18,18]   ,[221,461,26,6],[221,450,25,7]

twoNodesL=[]
twoRadiiL=[]

twoNodes=[]
twoRadii=[]

for Circle in twoCircles:
    #drawC(draw,Circle,'green')
    twoNodes.append(Circle[3])
    twoNodesL.append(math.log10(Circle[3]) )
    twoRadii.append(Circle[2])
    twoRadiiL.append(math.log10(Circle[2]) )

mTC, bTC = np.polyfit(twoNodesL,twoRadiiL, 1)

twoRadiiLF=[]
twoRadiiF=[]
for this in twoNodesL:
      twoRadiiLF.append(   this*mTC+bTC   )
      twoRadiiF.append(  10** (this*mTC+bTC)   )




if False:
    #plt.plot(nNodes, oneRadii, label='oneRadii')
   # plt.plot(nNodesL, oneRadii, label='oneRadii vs nodesL')
    #plt.plot(nNodesL, oneRadiiL, label='oneRadiiL vs nodesL')
   # plt.plot(nNodes, oneRadiiL, label='oneRadiiL vs nodesL')
    plt.plot(twoNodesL, twoRadii, label='twoRadii vs twonodes')
    plt.plot(twoNodesL, twoRadiiF, label='twoRadii F vs twonodes')
    #plt.plot(nNodes, oneRadiiF, label='oneRadii fit vs nodes')
    #plt.plot(nNodesL, logEvents, label='x:nodesL vs y:logEvents')
    #plt.plot(nNodesL, logEventsF, label='x:nodesL vs y:logEvents Fit')
    #plt.plot(nNodes, logEvents, label='x:nodes vs y:logEvents')

    plt.xlabel('number of nodes aaffected')
    #plt.ylabel('occurences Radius')
    plt.title('Number of racks affected=1 x:nodes vs y:')
    plt.show()




threeCircles = [[269, 565, 38,3], [269, 534.0, 31,4], [269, 510, 24,5], [269, 491, 21,6], [269, 474, 17,7]]

threeNodesL=[]
threeRadiiL=[]

threeNodes=[]
threeRadii=[]

for Circle in threeCircles:
    #drawC(draw,Circle,'blue')
    threeNodes.append(Circle[3])
    threeNodesL.append(math.log10(Circle[3]) )
    threeRadii.append(Circle[2])
    threeRadiiL.append(math.log10(Circle[2]) )



mThreeC, bThreeC = np.polyfit(threeNodesL,threeRadiiL, 1)

threeRadiiLF=[]
threeRadiiF=[]
for this in threeNodesL:
      threeRadiiLF.append(   this*mThreeC+bThreeC   )
      threeRadiiF.append(  10** (this*mThreeC+bThreeC)   )




if True:
    #plt.plot(nNodes, oneRadii, label='oneRadii')
   # plt.plot(nNodesL, oneRadii, label='oneRadii vs nodesL')
    #plt.plot(nNodesL, oneRadiiL, label='oneRadiiL vs nodesL')
   # plt.plot(nNodes, oneRadiiL, label='oneRadiiL vs nodesL')
    plt.plot(threeNodesL, threeRadii, label='threeRadii vs threenodes')
    plt.plot(threeNodesL, threeRadiiF, label='threeRadii F vs threenodes')
    #plt.plot(nNodes, oneRadiiF, label='oneRadii fit vs nodes')
    #plt.plot(nNodesL, logEvents, label='x:nodesL vs y:logEvents')
    #plt.plot(nNodesL, logEventsF, label='x:nodesL vs y:logEvents Fit')
    #plt.plot(nNodes, logEvents, label='x:nodes vs y:logEvents')

    plt.xlabel('number of nodes aaffected')
    #plt.ylabel('occurences Radius')
    plt.title('Number of racks affected=3 x:nodes vs y:')
    #plt.show()





def predictRone(theindex):

    return 10** (math.log10(theindex)*mNL+bNL)

def predictRtwo(theindex):

    return 10** (math.log10(theindex)*mTC+bTC)

mThC = -0.83 #-0.4791593263410262
bThC =  1.99#1.85066155247843
def predictRthree(theindex):

    return 10** (math.log10(theindex)*mThreeC+bThreeC)

def predictRfour(theindex):
     return 10** (math.log10(theindex)*four_mL+four_bL)

for n in range(4,10):
    Circle=[xloc(4),yloc(n),predictRfour(n)]
    print(Circle)
    #drawC(draw,Circle,'blue')


def predictRd(theindex):

    #return 10**(theindex*diag_m+diag_b)
     #return 10**(math.log10(theindex)*diag_mL+diag_bL  )
    if theindex<nmax:
        return 10**(theindex**2*diag_q+ theindex*diag_m+diag_b)
    else:
        return 2.5



for n in range(1,100):
    Circle=[xloc(n),yloc(n),predictRd(n)]
    #print(Circle)
    #drawC(draw,Circle,'purple')


#print(mTC,bTC)
for n in range(1,20):
    Circle=[139,yloc(n),predictRone(n)]
    #print(Circle)
    #drawC(draw,Circle,'red')

for n in range(2,20):
    Circle=[221,yloc(n),predictRtwo(n)]
    #print(Circle)
    #drawC(draw,Circle,'green')

threepredict=[]
for n in range(3,10):
    Circle=[269,yloc(n)+1,predictRthree(n)]
    threepredict.append(Circle)
    #print(Circle)
    #drawC(draw,Circle,'blue')
print(threepredict)
#img.save('marked_'+imgid)

img.save('marked_'+imgid)

if False:
    plt.plot(nNodes, oneRadii, label='oneRadii vs nodes')
   # plt.plot(nNodesL, oneRadii, label='oneRadii vs nodesL')
    #plt.plot(nNodesL, oneRadiiL, label='oneRadiiL vs nodesL')
   # plt.plot(nNodes, oneRadiiL, label='oneRadiiL vs nodesL')
    plt.plot(twoNodes, twoRadii, label='twoRadii vs nodes')
    #plt.plot(twoNodes, twoRadii, label='twoRadii vs nodes')
    #plt.plot(twoNodes, twoRadii, label='twoRadii vs twonodes')
    #plt.plot(twoNodesL, twoRadiiF, label='twoRadii F vs twonodes')
    #plt.plot(nNodes, oneRadiiF, label='oneRadii fit vs nodes')
    #plt.plot(nNodesL, logEvents, label='x:nodesL vs y:logEvents')
    #plt.plot(nNodesL, logEventsF, label='x:nodesL vs y:logEvents Fit')
    #plt.plot(nNodes, logEvents, label='x:nodes vs y:logEvents')

    plt.xlabel('number of nodes affected')
    #plt.ylabel('occurences Radius')
    plt.title('Radii')
    plt.legend()
    plt.show()