# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 03:00:44 2022

@author: nethm
"""

import cv2 as cv 
import numpy as np

im = cv.imread('img2.tif', 0)

f = np.fft.fft2(im)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
print (magnitude_spectrum)
magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)

res = np.hstack((im, magnitude_spectrum)) #stacking images side-by-side
cv.imwrite('res.png',res)