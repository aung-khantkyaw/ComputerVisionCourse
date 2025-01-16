import cv2
import numpy as np

image = cv2.imread('laziestant.jpg')
cv2.imshow('Original', image)

M = np.float32([[1,0,50],[0,1,100]])
shift = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Shifted Down 100 and Right 50', shift)

M = np.float32([[1,0,-50],[0,1,-50]])
shift = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Shifted up -50 and left -50', shift)

M = np.float32([[1,0,0],[0,1,100]])
shift = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow('Shifted Down 100', shift)

cv2.waitKey(0)