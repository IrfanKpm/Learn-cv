import cv2

'''
Countour detection is a popular computer vision technique used for 
   analyzing objects in an image Countours are useful tool for shape analysis,
   objects detection recogonise

A countour can be simply defined thats joins of set of points that enclosing an 
area having same color intensity.
'''

image = cv2.imread("./source/img6.png",0) 
img = cv2.imread("./source/img6.png") 

  # image preprocessing  
      # (1) -> Threshold based
      # (2) -> edge based



       # Threshold based
_, binary_image = cv2.threshold(image, 175, 255, cv2.THRESH_BINARY)
_, binary_image_inv = cv2.threshold(image, 220, 280, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(binary_image_inv, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

print(len(contours))

cv2.imshow("Original_img",img)
cv2.imshow("Gray_img",image)
cv2.imshow("Binary",binary_image)
cv2.imshow("Binary_INV",binary_image_inv)

cv2.waitKey()

cv2.destroyAllWindows()