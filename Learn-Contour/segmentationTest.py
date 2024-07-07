import cv2
import numpy as np

image = cv2.imread("./source/img5.png") 
img2 = image.copy()

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_hsv = (38,22,22)
higher_hsv = (160,255,255)

mask = cv2.inRange(hsv_image, lower_hsv, higher_hsv)

# Perform bitwise NOT operation directly on img2
cv2.bitwise_or(image, img2, mask)

# Display the images directly without storing the result
cv2.imshow("FRAME", image)
cv2.imshow("AND", img2)
cv2.imshow("MASK", mask)

cv2.waitKey()
cv2.destroyAllWindows()
