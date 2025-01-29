import cv2

import matplotlib.pyplot as plt

def cartoonize_image(image_path):

    img = cv2.imread(image_path)

    if img is None: raise ValueError("Failed to load image.")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, 5)

    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    color = cv2.bilateralFilter(img, 9, 300, 300)

    return cv2.bitwise_and(color, color, mask=edges)

# Image path (ensure it's uploaded or correctly specified)

image_path = 'test.jpg'

cartoon_image = cartoonize_image(image_path)

cartoon_image_rgb = cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2RGB)

plt.imshow(cartoon_image_rgb)

plt.axis('off')  # Hide axes

plt.show()