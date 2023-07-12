import numpy as np
import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)

img = img.astype(np.float32)

imgF = np.fft.fft2(img)

imgF = np.fft.fftshift(imgF)

imgReal = np.real(imgF)
imgIma = np.imag(imgF)
imgMag = np.sqrt(imgReal**2 + imgIma**2)
imgPhs = np.arctan2(imgIma, imgReal)

imgReallnv = imgMag*np.cos(imgPhs)
imgImalnv = imgMag*np.sin(imgPhs)

imgFlnv = imgReallnv + imgReallnv*1j

imgFlnv = np.fft.ifftshift(imgFlnv)
imglnv = np.fft.ifft2(imgFlnv)

imglnv = np.real(imglnv)
imglnv = imglnv.astype(np.uint8)

cv.imwrite('input.png', img)
cv.imwrite('output.png', imglnv)

imgMag = np.log(1+imgMag)
imgMag = cv.normalize(imgMag, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
cv.imwrite('magnitude.png', imgMag)