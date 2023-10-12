import numpy as np
import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)

laplacian = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize= 3)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize= 3)

sobelx = cv.normalize(sobelx, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
sobely = cv.normalize(sobely, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

cv.imwrite('sobelx.png', sobelx)
cv.imwrite('sobely.png', sobely)