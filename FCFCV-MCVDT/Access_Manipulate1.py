import cv2
img = cv2.imread('laziestant.jpg')
(b, g, r) = img[0, 0] #Row 0, Column 0 နေရာက BGR Color Code ကို ယူပြတာ
print("Blue = %d, Green= %d, Red = %d"%(b, g, r))
img[0, 0] = (0, 255, 0) #Row 0, Column 0 နေရာကို Green ပြောင်း
(b, g, r) = img[0, 0]
print("Blue = %d, Green= %d, Red = %d"%(b, g, r))
img[0:100, 0:100] = (255, 0, 0) #Row 0 - 100 , Column 0 - 100 နေရာကို Blue ပြောင်း
(b, g, r) = img[0:100, 0:100]
print("Blue = %d, Green= %d, Red = %d"%(b, g, r))
cv2.imshow('Image', img)
cv2.waitKey(0)