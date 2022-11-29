import random
import math
from PIL import Image
import numpy as np
from copy import copy, deepcopy
import time
import sys
from scipy.spatial import distance

def save_image(image, name):
    image.save("mod_"+name)
    
def open_image(string):
    im = Image.open(string)
    return im
    
def pixels_from_image(image):
    pix = image.load()
    return pix
    
def do_stuff():
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "help"):
            print("Usage: monochromator.py <file> [channel, default:0]")
            return
        if(sys.argv[1] != "help"):
            channel = 0
            if(len(sys.argv) > 2):
                channel = int(sys.argv[2])
            file = sys.argv[1]
            img = open_image(file)
            pixels = pixels_from_image(img)
            width, height = img.size
            for y in range(height):
                for x in range(width):
                    pixels[x,y] = (pixels[x,y][channel], pixels[x,y][channel], pixels[x,y][channel])
            save_image(img, str(channel) + "_" + file)
    
if __name__ == "__main__":
    do_stuff()
