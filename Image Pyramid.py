import cv2

img = cv2.imread('ca.jpg')

smaller = cv2.pyrDown(img)
larger = cv2.pyrUp(img)

cv2.imshow("Original Image",img)
cv2.imshow("Smaller Image", smaller)
cv2.imshow("Larger Image", larger)

cv2.waitKey()
cv2.destroyAllWindows()