# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:22:36 2019

@author: Viraj Mohile, NIT Surat, for ISB Hyderabad.
"""

from PIL import Image

# Morphological filtering
from skimage.morphology import opening
from skimage.morphology import disk
import pytesseract

# Data handling
import numpy as np

# Connected component filtering
#import cv2
def image_to_text():
    black = 0
    white = 255
    threshold = 160 
    # Open input image in grayscale mode and get its pixels.
    img = Image.open("captcha.png").convert("LA")
    pixels = np.array(img)[:,:,0]
    # Remove pixels above threshold
    pixels[pixels > threshold] = white
    pixels[pixels < threshold] = black
    # Morphological opening
    blobSize = 1 # Select the maximum radius of the blobs you would like to remove
    structureElement = disk(blobSize)  # you can define different shapes, here we take a disk shape
    # We need to invert the image such that black is background and white foreground to perform the opening
    pixels = np.invert(opening(np.invert(pixels), structureElement))
    # Create and save new image.
    newImg = Image.fromarray(pixels).convert('RGB')
    newImg.save("final.PNG")
    text = pytesseract.image_to_string("final.PNG")
    return text