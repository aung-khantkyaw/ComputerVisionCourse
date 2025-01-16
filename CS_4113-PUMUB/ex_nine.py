import cv2
import numpy as np
img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("original",img)
epsilon = 1e-10 #a small constant to avoid log(0)

frequency = np.fft.fft2(img) #frequency
mag_frequency = 20 * np.log(np.abs(frequency) + epsilon) #Calculate the magnitude spectrum
#mag_frequency = 20 * np.log1p(np.abs(frequency)) #Calculate the magnitude spectrum
mag_frequency = np.asarray(mag_frequency, np.uint8) #array
cv2.imshow("transform frequency", mag_frequency)

shift = np.fft.fftshift(frequency) #shift
mag_shift = 20 * np.log(np.abs(shift) + epsilon)
#mag_shift = 20 * np.log1p(np.abs(shift))
mag_shift = np.asarray(mag_shift, np.uint8)
cv2.imshow("transform frequency -> shift", mag_shift)

cv2.waitKey(0)
cv2.destroyAllWindows()