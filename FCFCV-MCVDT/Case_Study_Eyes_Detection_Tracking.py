import cv2
import imutils

camera = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')
while True:
    (grabbed, frame) = camera.read()
    if not grabbed:
        break
    frame = imutils.resize(frame, width=600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20), flags= cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in rects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()