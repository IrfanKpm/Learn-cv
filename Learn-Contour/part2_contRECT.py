import cv2


img = cv2.imread("./source/img5.png") 
image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

       # image preprocessing 
_, binary_image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
_, binary_image_inv = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY_INV)


contours, _ = cv2.findContours(binary_image_inv, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
sorted_contours = sorted(contours,key=cv2.contourArea,reverse=True)
sorted_contours = sorted_contours[1:] # to solve border_contour problem


for idx, contour in enumerate(sorted_contours,1):
    #cv2.drawContours(img, contour, -1, (0, 255, 0), 3)
    area = cv2.contourArea(contour)
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) # contour inside a rect ,but not min area
    

  # but here rect with resp. to min area   
rect = cv2.minAreaRect(sorted_contours[0])
box = cv2.boxPoints(rect).astype('int')
cv2.drawContours(img,[box], -1, (0, 255, 0), 3)


cv2.imshow("IMG",img)
cv2.imshow("Frame",binary_image_inv)
cv2.imshow("Binary",binary_image)


cv2.waitKey()

cv2.destroyAllWindows()