import cv2 as cv
import numpy as np

img_in = cv.imread('pic/dark.JPG', cv.IMREAD_GRAYSCALE)

gamma = 0.5
gamma_corrected = (img_in / 255)**gamma

gamma_corrected = gamma_corrected*255

img_out = np.array(gamma_corrected, dtype= np.uint8)

cv.imshow('Power-law', img_out)

cv.imwrite('pic/Demo_Pow_img_input.png', img_in)
cv.imwrite('pic/Demo_Pow_img_output.png', img_out)