import cv2 as cv
import numpy as np

def turn_to_bright(img):
    for i in range(0, 11):
        gamma = i
        gamma_corrected = (img / 255)**gamma

        gamma_corrected = gamma_corrected*255
        
        img_out = np.array(gamma_corrected, dtype= np.uint8)
        file_name = "pic/dark/Pow_img_output_gamma" + str(gamma) + ".png"
        cv.imwrite(file_name, img_out)