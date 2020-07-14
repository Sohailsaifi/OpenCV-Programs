#Scaling ,Resizing and Interplotation

import cv2
import numpy as np

img = cv2.imread('ca.jpg')
cv2.imshow("Original Image", img)
cv2.waitKey(0)

#To make the size of our image 3/4 of it's original image
img_scaled = cv2.resize(img, None, fx=0.75, fy=0.75)
cv2.imshow("Scaling-Linear Interplotation", img_scaled)
cv2.waitKey()

#To double the size of our image
img_scaled2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Scaling-Linear Interplotation", img_scaled2)
cv2.waitKey()

#To skew the re-sizing by setting exact dimension
img_scaled3 = cv2.resize(img, (900,400), interpolation=cv2.INTER_AREA)
cv2.imshow("Scaling-Linear Interplotation", img_scaled3)
cv2.waitKey()

cv2.destroyAllWindows()