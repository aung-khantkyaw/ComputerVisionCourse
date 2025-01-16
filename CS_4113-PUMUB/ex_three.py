import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('lena.png')
ret,timg = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.subplot (1,2,1)
plt.imshow (img)
plt.title('Original Image')
plt.subplot(1,2,2)
plt.imshow(timg)
plt.title('Thresholded Image')
plt.show()