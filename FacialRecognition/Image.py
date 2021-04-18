import cv2
from random import randrange

# Import Data
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Import image
img = cv2.imread('getty_475085221_970581970450081_64301.jpg')

# Greyscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect Faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

print(face_coordinates)

# Draws Rectangles around Faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128, 256), randrange(128, 256), randrange(128, 256)), 5)

# Display image
cv2.imshow('Face Detector', img)
cv2.waitKey()
