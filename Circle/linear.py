import numpy as np
import cv2 as cv

img = np.zeros([300, 300], dtype=np.uint8)

center = (150, 150)
end = 100
color = 255
start = 150
for x in range(center[0], center[0]+101):
    y = start
    start -= 1
    # print("y: %d, x: %d"% (y, x))
    img[y, x] = color

cv.imshow('Linear', img)
cv.waitKey(0)
cv.destroyAllWindows()
