import cv2
import numpy as np

img = cv2.imread('ca.jpg')

#Store height and width of the image

height, width = img.shape[:2]
print(height)
print(width)


quarter_height, quarter_width = height/4 , width/4
print(quarter_height)
print(quarter_width)

T = np.float32([[1,0,quarter_width],
                [0,1,quarter_height]])

print(T)

image_Translation = cv2.warpAffine(img, T, (width,height))
cv2.imshow("Original Image", img)
cv2.imshow("Translation", image_Translation)
cv2.waitKey(0)
cv2.destroyAllWindows()
