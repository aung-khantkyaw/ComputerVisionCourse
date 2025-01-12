import cv2
import numpy as np
img = cv2.imread('laziestant.jpg')
cv2.imshow('Original', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('L*A*B', lab)
cv2.waitKey(0)


# HSV - Hue Saturation Value
# H ကို 0 - 179 ပဲထားရ S နဲ့ V ကိုတော့ 0 - 255 ထားရ

# L*A*B - Lightness, Color Component Ranging from Green to Magenta, Color Component Ranging from Blue to Yellow
# L - Lightness ကို ထိန်းချုပ်ပြီး အောက်ကိုရောက်ရင် Black အပေါ်ကိုတက်ရင် White အလယ်က gray
# A - ညာဘက်အစွန်ဆုံးက Red ဘယ်ဘက်အစွန်ဆုံးက Green
# B - ညာဘက်အစွန်ဆုံးက Yellow ဘယ်ဘက်အစွန်ဆုံးက Blue