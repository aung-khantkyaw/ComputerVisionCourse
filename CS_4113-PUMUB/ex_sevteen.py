import cv2
import numpy as np

img = cv2.imread("hl.png")
kernel = np.ones((3, 3), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)

morphology_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
morphology_open_manual = cv2.dilate(erosion, kernel, iterations=1)

morphology_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
morphology_close_manual = cv2.erode(dilation, kernel, iterations=1)

cv2.imshow("Original", img)
# cv2.imshow("Erosion", erosion)
# cv2.imshow("Dilation", dilation)
cv2.imshow("Open", morphology_open)
cv2.imshow("Open Manual", morphology_open_manual)

cv2.imshow("Close", morphology_close)
cv2.imshow("Close Manual", morphology_close_manual)
cv2.waitKey(0)
