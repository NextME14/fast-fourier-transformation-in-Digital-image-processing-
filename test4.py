# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 01:26:25 2022

@author: nethm
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

im1 = cv.imread('wave1.jfif', 0)
im2 = cv.imread('wave2.jfif', 0)

im1_fourier = np.fft.fftshift(np.fft.fft2(im1))
im2_fourier = np.fft.fftshift(np.fft.fft2(im2))
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(im1_fourier)));
plt.imshow(np.log(abs(im2_fourier)));