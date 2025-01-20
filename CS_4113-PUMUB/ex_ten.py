import cv2
import numpy as np
import matplotlib.pyplot as plt

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
        H[u, v] = np.exp(-D**2/(2*D0**2))

high_pass = 1 - H

#Image Filter
#Low Pass Filter
Gaussian = img_shift*H
invert_shifted = np.fft.ifftshift(Gaussian)
low_pass_filter = np.fft.ifft2(invert_shifted)

#Low Pass Filter
Gaussian = img_shift*high_pass
invert_shifted = np.fft.ifftshift(Gaussian)
high_pass_filter = np.fft.ifft2(invert_shifted)

plt.subplot(131)
plt.imshow(img)
plt.title("Original Image")

plt.subplot(132)
plt.imshow(np.abs(low_pass_filter))
plt.title("Low Pass Filtered")

plt.subplot(133)
plt.imshow(np.abs(high_pass_filter))
plt.title("High Pass Filtered")

plt.show()

# Frequency => image ကို transform ပြောင်း => fft2(fftshift)