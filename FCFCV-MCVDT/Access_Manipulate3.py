import cv2
img = cv2.imread('laziestant.jpg')
b = img[0,0,0]
g = img[0,0,1]
r = img[0,0,2]
print("Blue = %d Green = %d Red = %d"%(b,g,r))
b = img.item(0,0,0)
g = img.item(0,0,1)
r = img.item(0,0,2)
print("Blue = %d Green = %d Red = %d"%(b,g,r))
img[0, 0] = [255, 0, 0]
(b, g, r) = img[0,0]
print("Blue = %d Green = %d Red = %d"%(b,g,r))