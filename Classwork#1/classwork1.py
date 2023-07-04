import numpy as np
import cv2 as cv

def filter():
    img = np.zeros([300, 300], dtype=np.uint8)
    
    center = (150, 150)
    end = 100
    color = 255
    start = 150
    for x in range(center[0], center[0]+101):
        if end < start:
            y = start
            start -= 1
            img[y, x] = color

        elif end > start:
            y = start
            start += 1
            img[y, x] = color
        
        elif end == start:
            y = end
            img[y, x] = color
            break
        
        else: 
            break

    cv.imwrite('Classwork#1/linear.png', img)
    return img

def convolution(img_size):
    filter_size = np.sum(img_size)
    kernels = img_size / (filter_size)
    img_in = cv.imread('Classwork#1/cat.jpeg', cv.IMREAD_GRAYSCALE)
    output = cv.filter2D(img_in, -1, kernels, borderType= cv.BORDER_REFLECT)
    return output

get_kernel = filter()
img_out = convolution(get_kernel)
cv.imwrite('Classwork#1/motionBlur.png', img_out)