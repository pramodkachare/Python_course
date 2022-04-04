import cv2
import numpy as np

##### Single photo click ###########

cap = cv2.VideoCapture(0)  # Initialize recorder object

# Camera will start and click a photo
ret, img = cap.read()

# Display the clicked photo
cv2.imshow('Frame', img)
# wait till user closes the image display window
cv2.waitKey(0)

# IMPORTANT: Release the camera
cap.release()


######## Continuous Video  ############
cap = cv2.VideoCapture(0)  # Initialize recorder object
while cap.isOpened():
    # Camera will start and click a photo
    ret, img = cap.read()
    
    if ret:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.rectangle(img, (100, 100), (60, 30), (255, 0, 0), 4)
        cv2.imshow('frame', img)
        
    if cv2.waitKey(int(1000/24)) & 0xFF == ord('q'):
        break

cap.release()
    
    
    
    
    
    
    
    
    
    
    