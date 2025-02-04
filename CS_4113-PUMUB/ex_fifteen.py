import cv2

cam = cv2.VideoCapture(0)

ret,frame = cam.read()


while(True):
    ret,frame = cam.read()
    cany = cv2.Canny(frame, 100, 200)
    lap = cv2.Laplacian(frame, cv2.CV_64F)
    sobel = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=3)
    cv2.imshow('canny', cany)
    cv2.imshow('lab', lap)
    cv2.imshow('sobel', sobel)
    if cv2.waitKey(3) == ord("q"):
        break


cam.release()

cv2.destroyAllWindows()