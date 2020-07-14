import cv2
#Method 1:


# img = cv2.imread('ca.jpg')
# cv2.imshow('Output Image', img)
# cv2.waitKey(0)
#
# gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow('Gray Scale Image', gray_image)
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()

#Method 2:


img = cv2.imread('ca.jpg',0)
cv2.imshow('Gray Scale Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
