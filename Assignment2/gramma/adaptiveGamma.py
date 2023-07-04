import cv2 as cv
import numpy as np
import os

def divide_image_into_blocks(image_path, block_size, overlap, save_folder):
    # Load the image
    image = cv.imread(image_path)
    height, width = image.shape[:2]
    stride = block_size - overlap

    # Create the save folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    count = 1

    for y in range(0, height - block_size + 1, stride):
        for x in range(0, width - block_size + 1, stride):
            block = image[y:y+block_size, x:x+block_size]
            save_path = os.path.join(save_folder, f"block_{count}.jpg")
            cv.imwrite(save_path, block)
            count += 1

def assemble_pictures(image_folder, block_size, overlap):
    images = []

    # Read all the images in the folder
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith(".jpg"):
            image_path = os.path.join(image_folder, filename)
            image = cv.imread(image_path)
            images.append(image)

    num_images = len(images)
    num_blocks_per_row = int((images[0].shape[1] - block_size) / (block_size - overlap)) + 1
    num_blocks_per_column = int((images[0].shape[0] - block_size) / (block_size - overlap)) + 1
    assembled_width = num_blocks_per_row * (block_size - overlap) + overlap
    assembled_height = num_blocks_per_column * (block_size - overlap) + overlap
    assembled_image = np.zeros((assembled_height, assembled_width, 3), dtype=np.uint8)

    count = 0

    # Assemble the blocks into the final image
    for i in range(num_blocks_per_column):
        for j in range(num_blocks_per_row):
            y_start = i * (block_size - overlap)
            y_end = y_start + block_size
            x_start = j * (block_size - overlap)
            x_end = x_start + block_size

            assembled_image[y_start:y_end, x_start:x_end] = images[count]
            count += 1

    return assembled_image

def adjust_gamma(user_gamma):
    lst = os.listdir("pic/test_gamma/blocking")
    number_files = len(lst)
    print(number_files)
    for i in range(1, number_files + 1):
        img_in = cv.imread('pic/test_gamma/blocking/block_{}.jpg'.format(i), cv.IMREAD_GRAYSCALE)
        mean_value = np.mean(img_in)
        if mean_value < user_gamma:
            get_gamma = 2
        else:
            get_gamma = 0.5

        gamma_corrected = (img_in / 255)**get_gamma

        gamma_corrected = gamma_corrected*255

        img_out = np.array(gamma_corrected, dtype= np.uint8)
        cv.imwrite(f'pic/test_gamma/Outblocking/outBlock_{i}.jpg', img_out)

# Example usage
image_path = "pic/test_gamma/dark.JPG"  # Replace with your image path
block_size = 64  # Size of each block
overlap = 16  # Overlapping region
save_folder = "pic/test_gamma/blocking"  # Replace with the desired save folder path
gamma = 1

blocking_path = 'pic/test_gamma/blocking'
outBlocking_path = 'pic/test_gamma/Outblocking'

blocking_path_isExist = os.path.exists(blocking_path)
outBlocking_path_isExist = os.path.exists(outBlocking_path)

if not blocking_path_isExist:
    divide_image_into_blocks(image_path, block_size, overlap, save_folder)

if not outBlocking_path_isExist:
    adjust_gamma(gamma)


# Example usage
assembled_image = assemble_pictures(outBlocking_path, block_size, overlap)
cv.imshow("Assembled Image", assembled_image)
cv.waitKey(0)
cv.destroyAllWindows()
