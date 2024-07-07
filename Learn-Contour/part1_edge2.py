import cv2

   # Edge based

img = cv2.imread("./source/img5.png") 
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



contours, hierarchy = cv2.findContours(gray_img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE) 

for i,count in enumerate(contours):
    if hierarchy[0][i][3] == -1: # first level contour > green 
        cv2.drawContours(img,[contours], -1, (0, 255, 0), 3)
    else:
        cv2.drawContours(img,[contours], -1, (0, 0, 255), 3)

    '''
    Actually in this example : it not worked properly.so i will explain  what this for loop do

    if 2 circle with same centre and c1 with r= 10 and c2 with r = 15
    then outer circle green,inner red
    '''

cv2.imshow("Original_img",img)



cv2.waitKey()
cv2.destroyAllWindows()