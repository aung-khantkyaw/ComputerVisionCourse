import cv2
img = cv2.imread('laziestant.jpg')
shape = img.shape #Image ရဲ့ Height,Width နဲ့ Color Channels တွေကို လို့ချင်လို့
print("shape", shape)
print("Height", shape[0])
print("Width", shape[1])
print("Channels", shape[2])
cv2.imshow('show', img)
cv2.waitKey(0)