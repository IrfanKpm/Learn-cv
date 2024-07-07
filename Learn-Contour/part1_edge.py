import cv2

   # Edge based

img = cv2.imread("./source/img7.png") 
blured_img = cv2.GaussianBlur(img,(5,5),15)
edge_img = cv2.Canny(blured_img,175,190)

#  cv2.RETR_EXTERNAL  -> outer line 
#  cv2.RETR_LIST   -> all 
      #  for more search : google...

contours, hierarchy = cv2.findContours(edge_img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE) 

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow("Original_img",img)
cv2.imshow("Blured_img",blured_img)
cv2.imshow("Edge_img",edge_img)


cv2.waitKey()
cv2.destroyAllWindows()