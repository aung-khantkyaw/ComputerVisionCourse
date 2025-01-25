import cv2
import numpy as np

image =cv2.imread('laziestant.jpg')
cv2.imshow('Original',image)

added = cv2.add(np.uint8([250]),np.uint8([10]))
subtracted = cv2.subtract(np.uint8([50]),np.uint8([100]))
print("Answer 1 addition: ", added)
print("Answer 2 subtraction: ", subtracted)

added = np.uint8([250]) + np.uint8([10])
subtracted = np.uint8([50]) - np.uint8([100])
print("Answer 3 addition: ", added)
print("Answer 4 subtraction: ", subtracted)
cv2.waitKey(0)

M = np.ones(image.shape,dtype="uint8")*75
Added = cv2.add(image,M)
cv2.imshow('Added',Added)
cv2.waitKey(0)
M = np.ones(image.shape,dtype="uint8")*100
Subtracted = cv2.subtract(image,M)
cv2.imshow('Subtracted',Subtracted)
cv2.waitKey(0)