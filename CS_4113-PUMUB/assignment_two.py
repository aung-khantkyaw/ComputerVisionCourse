import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_lowpass_mask(shape, cutoff):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2
    mask = np.zeros(shape, np.uint8)
    cv2.circle(mask, (ccol, crow), cutoff, 1, -1)
    return mask

def create_highpass_mask(shape, cutoff):
    lowpass_mask = create_lowpass_mask(shape, cutoff)
    highpass_mask = 1 - lowpass_mask
    return highpass_mask

def create_bandpass_mask(shape, cutoff_low, cutoff_high):
    mask = np.zeros(shape, np.uint8)
    cv2.circle(mask, (shape[1] // 2, shape[0] // 2), cutoff_high, 1, -1)
    cv2.circle(mask, (shape[1] // 2, shape[0] // 2), cutoff_low, 0, -1)
    return mask

img = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

cutoff_low = 30
cutoff_high = 60
cutoff = 45

# Lowpass
lowpass_mask = create_lowpass_mask(img.shape, cutoff)
fshift_low = fshift * lowpass_mask
img_back_low = np.fft.ifft2(np.fft.ifftshift(fshift_low))
img_back_low = np.abs(img_back_low).astype(np.uint8)

# Highpass
highpass_mask = create_highpass_mask(img.shape, cutoff)
fshift_high = fshift * highpass_mask
img_back_high = np.fft.ifft2(np.fft.ifftshift(fshift_high))
img_back_high = np.abs(img_back_high).astype(np.uint8)

# Bandpass
bandpass_mask = create_bandpass_mask(img.shape, cutoff_low, cutoff_high)
fshift_band = fshift * bandpass_mask
img_back_band = np.fft.ifft2(np.fft.ifftshift(fshift_band))
img_back_band = np.abs(img_back_band).astype(np.uint8)

# Image show
plt.figure(figsize=(15, 15))

plt.subplot(4, 2, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image')

plt.subplot(4, 2, 3), plt.imshow(img_back_low, cmap='gray'), plt.title('Lowpass Filtered')
plt.subplot(4, 2, 4), plt.imshow(np.log(1+np.abs(lowpass_mask)), cmap='gray'), plt.title('Lowpass Filter (Frequency Domain)')

plt.subplot(4, 2, 5), plt.imshow(img_back_high, cmap='gray'), plt.title('Highpass Filtered')
plt.subplot(4, 2, 6), plt.imshow(np.log(1+np.abs(highpass_mask)), cmap='gray'), plt.title('Highpass Filter (Frequency Domain)')

plt.subplot(4, 2, 7), plt.imshow(img_back_band, cmap='gray'), plt.title('Bandpass Filtered')
plt.subplot(4, 2, 8), plt.imshow(np.log(1+np.abs(bandpass_mask)), cmap='gray'), plt.title('Bandpass Filter (Frequency Domain)')

plt.show()