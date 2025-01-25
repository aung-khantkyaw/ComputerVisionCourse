import cv2

image = cv2.imread('laziestant.jpg')
StartY = 202
EndY = 375
StartX = 217
EndX = 390
face = image[StartY:EndY, StartX:EndX]
cv2.imshow('Face', face)
cv2.waitKey(0)