import cv2

img = cv2.imread('ca.jpg')

height, width = img.shape[:2]

#To get the starting pixel coordinates

start_row, start_col = int(height*0.25), int(width*0.25)

#To get the ending pixel coordinates

end_row, end_col = int(height*0.75), int(width*0.75)

#Using indexing to crop the image

cropped = img[start_row:end_row, start_col:end_col]

cv2.imshow("Original Image",img)
cv2.waitKey(0)

cv2.imshow("Cropped", cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()