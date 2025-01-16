import cv2
import numpy as np
blackimage = np.zeros((300, 300, 3), np.uint8)
cv2.imshow("Black Image", blackimage)
cv2.waitKey(0)

#Drawing Line
cv2.line(blackimage, (0,0), (300,300), (0,255,0), 1)
cv2.imshow("Line", blackimage)
cv2.waitKey(0)

#Drawing Rectangle
cv2.rectangle(blackimage, (100, 100), (150, 150), (255,0,0))
cv2.imshow("Rectangle", blackimage)
cv2.waitKey(0)
cv2.rectangle(blackimage, (200, 200), (250, 250), (0,0,255), -1)
cv2.imshow("Rectangle", blackimage)
cv2.waitKey(0)

#Drawing Circle
cv2.circle(blackimage, (150, 150), 50, (0,255,255), 1)
cv2.imshow("Circle", blackimage)
cv2.circle(blackimage, (50, 250), 20, (255,0,0), -1)
cv2.imshow("Circle", blackimage)
cv2.waitKey(0)
