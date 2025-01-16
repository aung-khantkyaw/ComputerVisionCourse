import cv2
import matplotlib.pyplot as plt
img = cv2.imread("lena.png")
ret,ting = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(ting)
plt.title('Ting')
plt.show()