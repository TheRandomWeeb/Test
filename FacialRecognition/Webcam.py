import cv2

# Import Data
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Import Video
webcam = cv2.VideoCapture(0)

while True:
    # Read Frame
    successful_frame_read, frame = webcam.read()

    # Greyscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    print(face_coordinates)

    # Draws Rectangles around Faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    # Display Video
    cv2.imshow('Face Detector', frame)
    key = cv2.waitKey(1)

    # Stop if ESC key is pressed
    if key==27:
        break

# Releases the webcam object
webcam.release()
