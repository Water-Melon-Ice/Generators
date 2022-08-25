from PIL import Image
from math import floor, ceil, sqrt, atan2, degrees
import numpy as np

xpix, ypix = 400, 400
pixels = np.zeros((ypix,xpix,2))

useAlpha = True
useShortMaxDistance = True

center = (ypix/2, xpix/2)

def distancefromcenter(y,x):
    return sqrt((y - center[0])**2 + (x-center[1])**2)

maxdistance = distancefromcenter(0,0) if not useShortMaxDistance else distancefromcenter(0,200)

def alphafromcenter(y,x):
    return 1.0 - (distancefromcenter(y,x) / maxdistance) 
    
def degreee(y,x):
    return degrees(atan2((y - center[0]) , (x - center[1]))) + 180
    
def getvalues(y,x):
    return degreee(y,x)


for i in range(ypix):
    for j in range(xpix):
        pixels[i,j] = ((getvalues(i,j)), alphafromcenter(i,j))
       


map = Image.new( mode = "RGBA", size = (xpix, ypix) )
pxn = map.load()
for y in range(ypix):
    for x in range(xpix):
        colorbase = [255,0,0,(255 * pixels[y,x,1]) if useAlpha else 255]
        degree = float(pixels[y,x,0])
        parts = degree / 60.0
        #blue up
        if(parts >= 1):
           parts -= 1
           colorbase[2] = 255
        else:
            colorbase[2] = 255 * (degree % 60.0) / 60.0
            pxn[y,x] = (int(colorbase[0]),int(colorbase[1]),int(colorbase[2]),int(colorbase[3]))
            continue
        #red down
        if(parts >= 1):
           parts -= 1
           colorbase[0] = 0
        else:
            colorbase[0] = 255 * (1 - (degree % 60.0) / 60.0)
            pxn[y,x] = (int(colorbase[0]),int(colorbase[1]),int(colorbase[2]),int(colorbase[3]))
            continue
        #green up 
        if(parts >= 1):
           parts -= 1
           colorbase[1] = 255
        else:
            colorbase[1] = 255 * (degree % 60.0) / 60.0
            pxn[y,x] = (int(colorbase[0]),int(colorbase[1]),int(colorbase[2]),int(colorbase[3]))
            continue
        #blue down
        if(parts >= 1):
           parts -= 1
           colorbase[2] = 0
        else:
            colorbase[2] = 255 * (1 - (degree % 60.0) / 60.0)
            pxn[y,x] = (int(colorbase[0]),int(colorbase[1]),int(colorbase[2]),int(colorbase[3]))
            continue
        #red up
        if(parts >= 1):
           parts -= 1
           colorbase[0] = 255
        else:
            colorbase[0] = 255 * (degree % 60.0) / 60.0
            pxn[y,x] = (int(colorbase[0]),int(colorbase[1]),int(colorbase[2]),int(colorbase[3]))
            continue
        #green down
        if(parts >= 1):
           parts -= 1
           colorbase[1] = 0
        else:
            colorbase[1] = 255 * (1 - (degree % 60.0) / 60.0)
        pxn[y,x] = (int(colorbase[0]),int(colorbase[1]),int(colorbase[2]),int(colorbase[3]))
        
        
map.show()
map.save("generated_image_" + str(xpix) + "-" + str(ypix) + ".png")