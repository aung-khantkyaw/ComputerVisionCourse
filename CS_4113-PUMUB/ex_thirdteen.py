import cv2

image = cv2.imread('lena.png',0)
rotateImage = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

#orb = cv2.ORB_create()

#kp, des = orb.detectAndCompute(image, None)
#rotate_kp, rotate_des = orb.detectAndCompute(rotateImage, None)

sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(image, None)
rotate_kp, rotate_des = sift.detectAndCompute(rotateImage, None)

matcher = cv2.BFMatcher()
matches = matcher.match(des, rotate_des)

compareImages = cv2.drawMatches(image, kp, rotateImage, rotate_kp, matches[:20], None)
cv2.imshow('matches', compareImages)
cv2.waitKey(0)