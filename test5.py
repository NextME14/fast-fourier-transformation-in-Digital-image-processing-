# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 01:51:45 2022

@author: nethm
"""
#RECTANLGE 

import cv2 as cv 
import numpy as np

im = cv.imread('square.jpg', 0)

f = np.fft.fft2(im)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
print (magnitude_spectrum)
magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)

res = np.hstack((im, magnitude_spectrum)) #stacking images side-by-side
cv.imwrite('res.png',res)

im2 = cv.imread('square2.jpg', 0)
fa = np.fft.fft2(im2)
fashift = np.fft.fftshift(fa)
magnitude_2 = 20*np.log(np.abs(fashift))
print (magnitude_2)
magnitude_2 = np.asarray(magnitude_2, dtype=np.uint8)

res2 = np.hstack((im2, magnitude_2)) #stacking images side-by-side
cv.imwrite('res2.png',res2)

im3 = cv.imread('square3.jpg', 0)
fa3 = np.fft.fft2(im2)
fa3shift = np.fft.fftshift(fa3)
magnitude_3 = 20*np.log(np.abs(fa3shift))
print (magnitude_3)
magnitude_3 = np.asarray(magnitude_3, dtype=np.uint8)

res3 = np.hstack((im3, magnitude_3)) #stacking images side-by-side
cv.imwrite('res3.png',res3)
