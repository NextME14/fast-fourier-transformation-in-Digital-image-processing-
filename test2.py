# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:48:47 2022

@author: nethm
"""

import cv2 as cv 
import numpy as np

im = cv.imread('wave1.jfif', 0)

f = np.fft.fft2(im)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
print (magnitude_spectrum)
magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)

res = np.hstack((im, magnitude_spectrum)) #stacking images side-by-side
cv.imwrite('res.png',res)


im2 = cv.imread('wave2.jfif', 0)
fa = np.fft.fft2(im2)
fashift = np.fft.fftshift(f)
magnitude_2 = 20*np.log(np.abs(fashift))
print (magnitude_2)
magnitude_2 = np.asarray(magnitude_2, dtype=np.uint8)

res2 = np.hstack((im2, magnitude_2)) #stacking images side-by-side
cv.imwrite('res2.png',res2)