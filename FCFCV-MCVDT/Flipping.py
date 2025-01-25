import cv2

image = cv2.imread('laziestant.jpg')
cv2.imshow('Original', image)
flipped_image = cv2.flip(image, 1)
cv2.imshow('Flipped Horizontal', flipped_image)
flipped_image = cv2.flip(image, 0)
cv2.imshow('Flipped Vertical', flipped_image)
flipped_image = cv2.flip(image, -1)
cv2.imshow('Flipped Horizontal and Vertical', flipped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()