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
            print("Usage: monochromator.py <options: help, pt: <file> [channel, default:0], sc: <file> <red%> <green%> <blue%>")
            return
        elif(sys.argv[1] == "pt"):
            if(len(sys.argv) > 2):
                red = 0.33
                green = 0.33
                blue = 0.33
                if(len(sys.argv) > 3):
                    red = int(sys.argv[3]) / 100.0
                if(len(sys.argv) > 4):
                    green = int(sys.argv[4]) / 100.0
                if(len(sys.argv) > 5):
                    blue = int(sys.argv[5]) / 100.0
                file = sys.argv[2]
                img = open_image(file)
                pixels = pixels_from_image(img)
                width, height = img.size
                for y in range(height):
                    for x in range(width):
                        color = int(pixels[x,y][0] * red + pixels[x,y][1] * green + pixels[x,y][2] * blue)
                        pixels[x,y] = (color, color, color)
                save_image(img, str(red) + "r_" + str(green) + "g_" + str(blue) + "b_" + file)
        elif(sys.argv[1] == "sc"):
            if(len(sys.argv) > 2):
                channel = 0
                if(len(sys.argv) > 3):
                    channel = int(sys.argv[3])
                file = sys.argv[2]
                img = open_image(file)
                pixels = pixels_from_image(img)
                width, height = img.size
                for y in range(height):
                    for x in range(width):
                        pixels[x,y] = (pixels[x,y][channel], pixels[x,y][channel], pixels[x,y][channel])
                save_image(img, str(channel) + "_" + file)
    
if __name__ == "__main__":
    do_stuff()
