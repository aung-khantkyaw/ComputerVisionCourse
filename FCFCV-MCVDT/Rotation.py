import cv2

image = cv2.imread('laziestant.jpg')
(h, w) = image.shape[:2]
(CX, CY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((CX, CY), 45, 1)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Original', image)
cv2.imshow('Rotated by 45 degree', rotated)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D((CX, CY), -90, 1)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotated by 90 degree', rotated)
cv2.waitKey(0)

M = cv2.getRotationMatrix2D((CX, CY), 180, 1)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotated by 180 degree', rotated)
cv2.waitKey(0)
