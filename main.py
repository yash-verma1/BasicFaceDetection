# Importing Libraries
import cv2
import sys

# Getting image path from supplied arguments
img_path = sys.argv[1]

# Reading image from path and converting to gray scale
img = cv2.imread(img_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initialising a Haar Cascade Classifier
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = classifier.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(30,30)
)

print("Found {0} faces!".format(len(faces)))

# Isolating identified faces
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

# Saving isolated faces on file system
status = cv2.imwrite('faces_isolated.jpg',img)

print("Image 'faces_isolated.jpg' has been saved to the file system: ",status)
