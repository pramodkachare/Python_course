import cv2
import os
import numpy as np

####### Classifier settings  ##########
file_path =  os.path.join('haarcascades', 'haarcascade_upperbody.xml')

classifier = cv2.CascadeClassifier(file_path)


######## Continuous Video  ############
cap = cv2.VideoCapture(0)  # Initialize recorder object
while cap.isOpened():
    # Camera will start and click a photo
    ret, img = cap.read()
    
    if ret:
        faces = classifier.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.2, 5)

        for face in faces:   
            cv2.rectangle(img, (face[0], face[1]), (face[0]+face[2], face[1]+face[2]), 
                          (0, 0, 255), 4)
        
        cv2.imshow('frame', img)
        
    if cv2.waitKey(int(1000/24)) & 0xFF == ord('q'):
        break

cap.release()
    
# Display the clicked photo
cv2.imshow('Frame', img)
# wait till user closes the image display window
cv2.waitKey(0)

# IMPORTANT: Release the camera
cap.release()
