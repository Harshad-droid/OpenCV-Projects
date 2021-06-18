import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  # Load the cascade

img = cv2.imread('tester.jpg')   # Read the input image

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # Convert into grayscale

faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # Detect faces

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()