import cv2


img = cv2.imread("./source/img6.png") 
img2 = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,binary_img = cv2.threshold(gray,230,255,cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

cnt = contours[0]
hull = cv2.convexHull(cnt)

cv2.drawContours(img, [cnt], -1, (0,255,0), 3)
cv2.drawContours(img2,[hull], -1, (0,0,255), 3)

cv2.imshow("IMG",img)
cv2.imshow("BIN_INV",binary_img)
cv2.imshow("IMG2",img2)

cv2.waitKey()
cv2.destroyAllWindows()