import cv2
import os
import numpy as np

####### Classifier settings  ##########
file_path =  os.path.join('haarcascades', 'haarcascade_frontalface_default.xml')

classifier = cv2.CascadeClassifier(file_path)


##### Single photo click ###########

cap = cv2.VideoCapture(0)  # Initialize recorder object

# Camera will start and click a photo
ret, img = cap.read()

faces = classifier.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.2, 5)

for face in faces:   
    cv2.rectangle(img, (face[0], face[1]), (face[0]+face[2], face[1]+face[2]), 
                  (0, 0, 255), 4)
#for (x, y, h, w) in faces:
    # cv2.rectangle(img, (x, y, (x+h, y+w), (0, 0, 255), 4)
    
# Display the clicked photo
cv2.imshow('Frame', img)
# wait till user closes the image display window
cv2.waitKey(0)

# IMPORTANT: Release the camera
cap.release()
