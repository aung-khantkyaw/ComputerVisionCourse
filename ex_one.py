import numpy as  np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread("lena.png")
# ret,ting = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret,ting = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)

cv2.imshow("original",img)
cv2.imshow("Threshshow image",ting)
cv2.waitKey(0)
cv2.destroyAllWindows()