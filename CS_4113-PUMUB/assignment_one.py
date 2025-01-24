import cv2
import numpy as np

def gamma_correction(image, gamma):
    """Applies gamma correction to an image. The gamma value (float). Gamma < 1 makes the image brighter, gamma > 1 makes it darker. A gamma of 1 does nothing."""
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    corrected_image = cv2.LUT(image, table)
    return corrected_image

def color_sharpening(image):
    """Sharpens a color image using a basic sharpening kernel."""
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image

def histogram_equalization(image):
    """Equalizes the histogram of a color image (on each channel)."""
    channels = cv2.split(image)
    equalized_channels = []
    for channel in channels:
        equalized_channel = cv2.equalizeHist(channel)
        equalized_channels.append(equalized_channel)
    equalized_image = cv2.merge(equalized_channels)
    return equalized_image

# Input image
image = cv2.imread('lena.png')

# Function call
gamma_corrected = gamma_correction(image, 2.2)
sharpened = color_sharpening(image)
equalized = histogram_equalization(image)

# Image show
cv2.imshow("Original", image)
cv2.imshow("Gamma Corrected", gamma_corrected)
cv2.imshow("Sharpened", sharpened)
cv2.imshow("Histogram Equalized", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()
