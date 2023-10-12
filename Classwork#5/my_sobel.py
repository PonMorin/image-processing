import numpy as np
import cv2 as cv

def sobel_filter(image):
    # gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    sobel_x = np.array([[1, 0, -1],
                        [2, 0, -2],
                        [1, 0, -1]])

    sobel_y = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]])
    
    grad_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize= 3)
    # grad_y = cv.filter2D(image, -1, sobel_y)

    sobelImg_x = cv.normalize(grad_x, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    cv.imwrite('sobelimg_X.png', sobelImg_x)
    return sobelImg_x, sobel_x


def fourier_filter(img):
    # img = img.astype(np.float32)

    imgF = np.fft.fft2(img)

    # imgF = np.fft.fftshift(imgF)

    # imgReal = np.real(imgF)
    # imgIma = np.imag(imgF)
    # imgMag = np.sqrt(imgReal**2 + imgIma**2)
    # imgPhs = np.arctan2(imgIma, imgReal)

    # imgMag = np.log(1+imgMag)
    # imgMag = cv.normalize(imgMag, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    # cv.imwrite('input.png', imgReal)
    # cv.imwrite('magnitude.png', imgMag)
    return imgF

def dot_product(img, filter_img):#dot_product(A,B) ผล ไก้ a x b
    dot = img * filter_img
    return dot

def convert_to_spatial(con_img):
    imglnv = np.fft.fftshift(con_img)
    imglnv = np.fft.ifft2(con_img)
    imglnv = np.real(imglnv)
    # imglnv = imglnv.astype(np.uint8)
    convert_img = cv.normalize(imglnv, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    cv.imwrite('output.png', convert_img)
    return convert_img

if __name__ == '__main__':
    img = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)
    sobelImg, sobelFilter = sobel_filter(img)
    fourier_img = fourier_filter(img)

    h, w = fourier_img.shape
    pad_height = max(0, h - sobelFilter.shape[0])
    pad_width = max(0, w - sobelFilter.shape[1])
    padded_array = np.pad(sobelFilter, ((0, pad_height), (0, pad_width)), mode='constant', constant_values=0)

    con_filter = np.fft.ifftshift(padded_array)

    fourier_filter = fourier_filter(padded_array)
    product = dot_product(fourier_img, fourier_filter)
    con_img = convert_to_spatial(product)

    compare_img = cv.hconcat([sobelImg, con_img])
    cv.imshow('Sapatial and Frequency', compare_img)
    cv.waitKey(0)
    cv.destroyAllWindows()