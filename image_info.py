import cv2

img = cv2.imread('ca.jpg')
cv2.imshow('Output Image', img)

print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()