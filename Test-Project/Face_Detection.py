import cv2

import matplotlib.pyplot as plt

def detect_faces(image_path):

    img = cv2.imread(image_path)

    if img is None: raise ValueError("Failed to load image.")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return img

# Image path (ensure it's uploaded or correctly specified)

image_path = 'test.jpg'

# Detect faces

face_image = detect_faces(image_path)

face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

# Display the image with detected faces

plt.imshow(face_image_rgb)

plt.axis('off')  # Hide axes

plt.show()