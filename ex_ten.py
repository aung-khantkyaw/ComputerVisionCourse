import cv2
import numpy as np

img = cv2.imread('lena.png', 0)
img_frequency = np.fft.fft2(img)
img_shift = np.fft.fftshift(img_frequency)

M,N = img.shape
H = np.zeros((M,N), np.float32)

#Create Gaussian Filter H(u,v)
D0 = 10
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        H = np.exp(-D**2/(2*D0**2))

#Image Filter
Gaussian = img_shift*H
invert_shifted = np.fft.ifftshift(Gaussian)
Filter = np.fft.ifft2(invert_shifted)

cv2.imshow('Original', img)
cv2.imshow('Filtered', np.abs(Filter))
cv2.waitKey(0)
cv2.destroyAllWindows()