import cv2
import numpy as np
img = cv2.imread('noisesp.PNG')
frequency = np.fft.fft2(img)
shift = np.fft.fftshift(frequency)
mgspec = np.log(np.abs(shift))
cv2.imshow("original",img)
cv2.imshow("transform", mgspec)
cv2.waitKey(0)