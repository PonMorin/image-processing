import numpy as np
import cv2 as cv

def sobel_filter(image):
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

    sobel_y = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]])
    
    grad_x = cv.filter2D(image, -1, sobel_x)
    grad_y = cv.filter2D(image, -1, sobel_y)

    cv.imwrite('sobelimg_X.png', grad_x)
    return grad_x, sobel_x

def fourier_transform(img):
    img = img.astype(np.float32)
    imgF = np.fft.fft2(img)
    # imgF = np.fft.fftshift(imgF)
    return imgF

def dot_product(fourier_img, fourier_sobel_filter):
    dot = fourier_img * fourier_sobel_filter
    return dot

def inverse_fourier_transform(con_img):
    imglnv = np.fft.ifft2(con_img)
    imglnv = np.real(imglnv)
    imglnv = imglnv.astype(np.uint8)
    cv.imwrite('output.png', imglnv)

if __name__ == '__main__':
    img = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)
    sobel_output, sobelFilter = sobel_filter(img)

    # Convert Sobel filter to the frequency domain
    fourier_sobel_filter = fourier_transform(sobelFilter)

    # Convert the input image to the frequency domain
    fourier_img = fourier_transform(img)

    h, w = fourier_img.shape
    pad_height = max(0, h - fourier_sobel_filter.shape[0])
    pad_width = max(0, w - fourier_sobel_filter.shape[1])
    padded_array = np.pad(fourier_sobel_filter, ((0, pad_height), (0, pad_width)), mode='constant', constant_values=0)

    # Perform the dot product in the frequency domain
    product = dot_product(fourier_img, padded_array)

    # Convert the result back to the spatial domain
    inverse_fourier_transform(product)
