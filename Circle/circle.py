import numpy as np
import cv2 as cv

img = np.zeros([300, 300], dtype=np.uint8)

center = (150, 150)
radius = 100
color = 255

for y in range(300):
    for x in range(300):
        getRange = (x - center[0]) ** 2 + (y - center[1]) ** 2
        if getRange <= radius ** 2:
            img[y, x] = color

cv.imshow('Circle', img)
cv.waitKey(0)
cv.destroyAllWindows()
