from skimage.metrics import structural_similarity as ssim
import cv2

# Load the images
image1 = cv2.imread('image-processing/Classwork#3/cat.jpg')# Replace with the path to the original image
image2 = cv2.imread('image-processing/Classwork#3/adjustNoise.png')  # Replace with the path to the adjusted image

# Convert the images to grayscale
image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Calculate the SSIM
ssim_value = ssim(image1_gray, image2_gray, data_range=image2_gray.max() - image2_gray.min())

# Print the SSIM value
print('SSIM:', ssim_value)
