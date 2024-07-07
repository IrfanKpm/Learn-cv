import cv2

   # Edge based

img = cv2.imread("./source/img8.png") 
blured_img = cv2.GaussianBlur(img,(5,5),10)
edge_img = cv2.Canny(blured_img,175,190)



contours, hierarchy = cv2.findContours(edge_img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE) 

cv2.drawContours(img, contours, -1, (50, 50, 50), 3)

for contour in contours:
    M = cv2.moments(contour)
    print(M['m00'])
    if M['m00'] != 0:
        # Calculate the centroid
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(img,(cx,cy),8,(125,125,125),-1)


cv2.imshow("Original_img",img)
cv2.imshow("Blured_img",blured_img)
cv2.imshow("Edge_img",edge_img)


cv2.waitKey()
cv2.destroyAllWindows()