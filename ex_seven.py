import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('noisesp.PNG')
kernel = np.ones((3,3), np.float32) / 9
kernel1 = np.array(([0,0,0],[0,1,0],[0,0,0]), np.float32)
kernel2 = np.array(([0,-1,0],[-1,4,-1],[0,-1,0]), np.float32) #edge dection
kernel3 = np.array(([0,-1,0],[-1,6,-1],[0,-1,0]), np.float32) #sharpen
kernel4 = np.ones((5,5),np.float32)/25 #blur

filter = cv2.filter2D(img,-1,kernel)
filter1 = cv2.filter2D(img,-1,kernel1)
filter2 = cv2.filter2D(img,-1,kernel2)
filter3 = cv2.filter2D(img,-1,kernel3)
filter4 = cv2.filter2D(img,-1,kernel4)

plt.subplot(2, 3, 1)
plt.imshow (img)
plt.title('Original Image')

plt.subplot(2, 3, 2)
plt.imshow (filter)
plt.title('Filter Image')

plt.subplot(2, 3, 3)
plt.imshow (filter1)
plt.title('Filter1 Image')

plt.subplot(2, 3, 4)
plt.imshow (filter2)
plt.title('Filter2 Image')

plt.subplot(2, 3, 5)
plt.imshow (filter3)
plt.title('Filter3 Image')

plt.subplot(2, 3, 6)
plt.imshow (filter4)
plt.title('Filter4 Image')


plt.show()