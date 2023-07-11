import cv2 as cv
import numpy as np
import random
from skimage.metrics import structural_similarity as ssim

def make_noise(images):
    density_salt = 0.1
    density_pepper = 0.1

    number_of_white_pixel = int(density_salt * (images.shape[0] * images.shape[1]))

    for i in range(number_of_white_pixel):
        y_coord = random.randint(0, images.shape[0] - 1)
        x_coord = random.randint(0, images.shape[1] - 1)
        images[y_coord][x_coord] = 255

    number_of_black_pixel = int(density_pepper * (images.shape[0] * images.shape[1]))

    for i in range(number_of_black_pixel):
        y_coord = random.randint(0, images.shape[0] - 1)
        x_coord = random.randint(0, images.shape[1] - 1)
        images[y_coord][x_coord] = 0
    
    cv.imwrite('image-processing/Classwork#3/sp.png', images)


def compare_pic_ssim():
    image1 = cv.imread('image-processing/Classwork#3/cat.jpg')
    image1_gray = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)

    image2 = cv.imread('image-processing/Classwork#3/sp.png')
    for i in range(1, 10, 2):
        output = cv.medianBlur(image2, i)
        image2_gray = cv.cvtColor(output, cv.COLOR_BGR2GRAY)
        ssim_value = ssim(image1_gray, image2_gray, data_range=image2_gray.max() - image2_gray.min())
        
        if 0.9 < ssim_value <= 1:
            print('Filter size {} is better'.format(i))
            cv.imwrite('image-processing/Classwork#3/result.png', output)
        
        result = np.concatenate((image1_gray, image2_gray), axis=1)
        cv.imshow('Compare Image', result)
        cv.waitKey(0)
        cv.destroyAllWindows()


img = cv.imread('image-processing/Classwork#3/cat.jpg', cv.IMREAD_GRAYSCALE)
noise_img = make_noise(img)
compare_pic = compare_pic_ssim()