import cv2

img = cv2.imread('lena.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray, 100, 200)
_ , edges = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('img', edges)

return_contours, _ = cv2.findContours(edges, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
output = cv2.drawContours(img, return_contours, -1, (0, 255, 0), 3)
cv2.imshow('contours', output)

cv2.waitKey(0)