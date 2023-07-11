import cv2
import numpy as np

# Load the original image and adjusted image
original_image = cv2.imread('image-processing/Classwork#3/cat.jpg')# Replace with the path to the original image
adjusted_image = cv2.imread('image-processing/Classwork#3/cat.jpg')  # Replace with the path to the adjusted image

# Convert images to grayscale
original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
adjusted_gray = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2GRAY)

# Calculate histograms
hist_original = cv2.calcHist([original_gray], [0], None, [256], [0, 256])
hist_adjusted = cv2.calcHist([adjusted_gray], [0], None, [256], [0, 256])

# Normalize histograms
hist_original = cv2.normalize(hist_original, hist_original, norm_type=cv2.NORM_L1)
hist_adjusted = cv2.normalize(hist_adjusted, hist_adjusted, norm_type=cv2.NORM_L1)

# Calculate histogram intersection
hist_intersection = cv2.compareHist(hist_original, hist_adjusted, cv2.HISTCMP_INTERSECT)

# Print the histogram intersection value
print('Histogram Intersection:', hist_intersection)
