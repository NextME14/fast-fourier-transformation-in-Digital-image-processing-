# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:07:35 2022

@author: nethm
"""

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

#Generate a 2D sine wave image
x = np.arange(256)  # generate values from 0 to 255 (our image size)
y = np.sin(2 * np.pi * x / 30)  #calculate sine of x values
#Divide by a smaller number above to increase the frequency.
y += max(y) # offset sine wave by the max value to go out of negative range of sine 

#Generate a 256x256 image (2D array of the sine wave)
img = np.array([[y[j]*127 for j in range(256)] for i in range(256)], dtype=np.uint8) # create 2-D array of sine-wave

#plt.imshow(img)
#img = np.rot90(img)  #Rotate img by 90 degrees