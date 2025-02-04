import cv2
import matplotlib.pyplot as plt
import numpy as np
# import matplotlib.image as plt

img = cv2.imread("lena.png")
img2 = cv2.imread("sf2.jpg")
# img2 = cv2.rotate(img2,cv2.ROTATE_90_CLOCKWISE)

canny = cv2.Canny(img,100,200)
# cv2.imshow("canny",canny)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
# cv2.imshow("laplacian",laplacian)

sobel = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
# cv2.imshow("sobel",sobel)

plt.subplot(1,3,1)
plt.imshow(canny)
plt.title('canny Image')
plt.subplot(1,3,2)
plt.imshow(laplacian)
plt.title('laplacian Image')
plt.subplot(1,3,3)
plt.imshow(sobel)
plt.title('sobel Image')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()