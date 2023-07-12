import cv2
import numpy as np

# Load the original image and adjusted image
original_image = cv2.imread('image-processing/Classwork#3/cat.jpg')# Replace with the path to the original image
adjusted_image = cv2.imread('image-processing/Classwork#3/sp.png')  # Replace with the path to the adjusted image

mse = np.mean((original_image - adjusted_image) ** 2)

# Calculate PSNR
psnr = 10 * np.log10((255 ** 2) / mse)

# Define threshold range
threshold_low = 30
threshold_high = 40

# Check if PSNR is within the threshold range
if threshold_low <= psnr <= threshold_high:
    print(psnr)
    print('PSNR is closely matched.')
else:
    print('PSNR is not within the desired range.')