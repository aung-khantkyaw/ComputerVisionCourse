import cv2

img = cv2.imread('aheimage.png')
gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equimg = cv2.equalizeHist(gimg)
clahe = cv2.createCLAHE(2.0, (8,8))
adimg = clahe.apply(gimg)

cv2.imshow('Original', img)
#cv2.imshow('Grayscale', gimg)
cv2.imshow('EqualizeHist', equimg)
cv2.imshow('CLAHE', adimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

