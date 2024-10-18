# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:12:26 2024

@author: youhe
"""

import cv2 as cv
import sys

img = cv.imread("C:/Users/youhe/OneDrive/Desktop/4-2/CV/OpenCV/MongJi.png")

if img is None:
    sys.exit('No file')
    
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh, binary_otsu_img) = cv.threshold(gray, 120, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

print('The Best Threshold Value obtained by Otsu = ', thresh)

cv.imwrite('C:/Users/youhe/OneDrive/Desktop/4-2/CV/OpenCV/MongJi_bin_otsu.png', binary_otsu_img)

cv.imshow('Gray Image', gray)
cv.imshow('Binary Otsu Image', binary_otsu_img)

cv.waitKey()
cv.destroyAllWindows()
