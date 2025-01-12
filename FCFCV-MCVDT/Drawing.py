import cv2
import numpy as np
blackimage = np.zeros((300, 300, 3), np.uint8)
cv2.imshow("blackimage", blackimage)
cv2.waitKey(0)
cv2.line(blackimage, (0,0))