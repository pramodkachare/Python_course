import cv2
import numpy as np

print('OpenCV version:', cv2.__version__)

img = cv2.imread('chrome_logo.png', cv2.IMREAD_COLOR)

# img[height, width, channels]
# cv2.imshow('Google chrome logo', img[100:500, 100:350, 0:2])
# cv2.waitKey(0)   # time in milliseconds


############# Line #############
# Color -> Blue, Green, Red
# cv2.line(image, start_point, stop_point, color, linewidth)
cv2.line(img, (0, 0), (512, 396), (100, 155, 240), 40)

############ Rectangle #########
#cv2.recangle(image, start_point, (height, width), color, linewidth)
cv2.rectangle(img, (100, 100), (60, 30), (255, 0, 0), 4)

############ Circle #########
# cv2.cicle(image, center_location, radius, color, thickness)
cv2.circle(img, (150, 300), 60, (0, 255, 0), 4)

############ Ellipse #########
# cv2.ellipse(image, centre location, major axis length, minor axis length, start angle of rotation, end angle of rotation,)
cv2.ellipse(img, (400, 200), (100, 60), 0, 0, 360, (0, 0, 255), 4)

############ Polygon #########
pts = np.array([[100, 50], [200, 300], [400, 400], [500, 500]])
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 240, 240), 10)

############ Text #############
cv2.putText(img, 'Pramod', (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, 
            (100, 100,100), 10, cv2.LINE_AA)
cv2.imshow('Google chrome logo', img)


cv2.waitKey(0)   # time in milliseconds
