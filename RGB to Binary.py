import cv2

img = cv2.imread('ca.jpg',0)
cv2.imshow('Output Image', img)
cv2.waitKey(0)

ret, bw = cv2.threshold(img, 127,255, cv2.THRESH_BINARY)

cv2.imshow('Binary Image', bw)

cv2.waitKey(0)

cv2.destroyAllWindows()