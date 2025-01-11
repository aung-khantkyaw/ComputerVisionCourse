import cv2
import matplotlib.pyplot as plt
img = cv2.imread("bright.jpg")
ret,ting = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Original Image')
plt.subplot(1, 3, 2)
plt.imshow(ting)
plt.title('Ting')

plt.subplot(1, 3, 3)
plt.imshow(ting)
plt.title('Ting')

plt.subplot(2, 3, 1)
plt.imshow(ting)
plt.title('Ting')

plt.subplot(2, 3, 2)
plt.imshow(ting)
plt.title('Ting')

plt.subplot(2, 3, 3)
plt.imshow(ting)
plt.title('Ting')

plt.show()