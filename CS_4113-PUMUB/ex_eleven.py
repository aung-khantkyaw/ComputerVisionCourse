#Detector Methods (Harris, SIFT, FAST)

import cv2
import numpy as np

image = cv2.imread('laziestant.jpeg')
gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#gray = np.float32(gray)

#harris = cv2.cornerHarris(gray,2,3,0.04)
#image[harris>0.01*harris.max()]=[255, 0, 255]
#cv2.imshow("Harris", image)

#sift = cv2.SIFT_create()
#keypoint = sift.detect(gray, None)
#image = cv2.drawKeypoints(image, keypoint, None)
#cv2.imshow('SIFT', image)

fast = cv2.FastFeatureDetector_create()
keypoint = fast.detect(gray, None)
image = cv2.drawKeypoints(image, keypoint, None)
cv2.imwrite('keypoints.jpg', image)
cv2.imshow('FAST', image)

cv2.waitKey(0)