import cv2

image = cv2.imread('laziestant.jpg')
h, w = image.shape[:2]
print("Width =%d, Height =%d" % (w, h))
ratio = 600.0/w
dimension = (600, int(h * ratio))
resized_width = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
cv2.imshow("Original", image)
cv2.imshow('resized_image', resized_width)
cv2.waitKey(0)
ratio = 200.0/h
dimension = (int(w * ratio), 200)
resized_height = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
cv2.imshow('resized_image', resized_height)
cv2.waitKey(0)
ratio = 500.0/h
dimension = (500, int(h * ratio))
methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
for(method_name, method) in methods:
    resized = cv2.resize(image, dimension, interpolation=method)
    cv2.imshow("Method = %s"%method_name, resized)
    cv2.waitKey(0)