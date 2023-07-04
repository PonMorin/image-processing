import cv2 as cv
import os
import numpy as np

def assemble_images(image_folder, block_size, overlap):
    images = []

    # Read all the images in the folder
    lst = os.listdir(image_folder)
    number_files = len(lst)
    for filename in range(1, number_files + 1):
        image_path = os.path.join(image_folder, 'outBlock_{}.jpg'.format(filename))
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

# Example usage
image_folder = "pic/test_gamma/Outblocking"  # Replace with the folder path containing the images
block_size = 64  # Size of each block
overlap = 16  # Overlapping region

assembled_image = assemble_images(image_folder, block_size, overlap)

cv.imwrite('pic/test_output.png', assembled_image)
