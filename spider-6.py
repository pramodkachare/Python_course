import cv2

print('OpenCV version:', cv2.__version__)

img = cv2.imread('chrome_logo.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Google chrome logo', img)

k = cv2.waitKey(0)   # time in milliseconds

if k == ord('s'):   # Check if key ('s') is pressed on keyboard
    cv2.imwrite('demo.png', img)


################################################
cap = cv2.VideoCapture('google_work.mp4')  # Load video file

while cap.isOpened():  # as long as video file is opened
    ret, frame = cap.read()   # read a image
    
    if ret:  # if frame or image is available
        cv2.imshow('frame', frame)
        cv2.waitKey(10)  # frame rate (rate at which video is played)
    else:   # if frame is not available then stop while loop
        break
        
cap.release()  # close the file
cv2.destroyAllWindows()  # close all opened windows

        