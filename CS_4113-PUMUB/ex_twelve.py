"""
Descriptor Methods (SIFT, ORB => Work Both Detector and Descriptor)
ORB has two parts, first is FAST for Detector and the second is BRIEF for Descriptor
"""
import cv2
import numpy as np

image = cv2.imread('laziestant.jpeg')
gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#sift = cv2.SIFT_create(30)
#keypoint, des = sift.detectAndCompute(gray, None)
#image = cv2.drawKeypoints(image, keypoint, None)
#cv2.imshow('SIFT', image)

orb = cv2.ORB_create()
kp, des = orb.detectAndCompute(gray, None)
image = cv2.drawKeypoints(image, kp, None)
cv2.imshow('ORB', image)

cv2.waitKey(0)

