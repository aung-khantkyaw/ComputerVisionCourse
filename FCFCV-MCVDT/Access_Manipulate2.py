import cv2
img = cv2.imread('laziestant.jpg')
cX, cY = img.shape[1]//2, img.shape[0]//2 #center X နဲ့ center Y ကိုရှာ
EndX, EndY = img.shape[1], img.shape[0] #image ရဲ့ Width နဲ့ Height ကိုရှာ
TL = img[0:cY, 0:cX] #TopLeft
TR = img[0:cY, cX:EndX] #TopRight
BL = img[cY:EndY, 0:cX] #BottomLeft
BR = img[cY:EndY, cX:EndX] #BottomRight
cv2.imshow('TL', TL)
cv2.imshow('TR', TR)
cv2.imshow('BL', BL)
cv2.imshow('BR', BR)
cv2.waitKey(0)