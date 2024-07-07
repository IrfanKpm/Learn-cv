import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cv2.namedWindow('Trackbars')

def nothing(x):
    pass

# Create trackbars for lower and upper HSV values
cv2.createTrackbar('Hue Lower', 'Trackbars', 0, 179, nothing)
cv2.createTrackbar('Saturation Lower', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Value Lower', 'Trackbars', 0, 255, nothing)
cv2.createTrackbar('Hue Upper', 'Trackbars', 179, 179, nothing)
cv2.createTrackbar('Saturation Upper', 'Trackbars', 255, 255, nothing)
cv2.createTrackbar('Value Upper', 'Trackbars', 255, 255, nothing)

while True:
    status,frame = cap.read()
    if not status:
        continue
    h, w = frame.shape[:2]
    n = 1.4
    frame = cv2.resize(frame,(int(w/n),int(h/n)))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Get current trackbar positions
    h_lower = cv2.getTrackbarPos('Hue Lower', 'Trackbars')
    s_lower = cv2.getTrackbarPos('Saturation Lower', 'Trackbars')
    v_lower = cv2.getTrackbarPos('Value Lower', 'Trackbars')
    h_upper = cv2.getTrackbarPos('Hue Upper', 'Trackbars')
    s_upper = cv2.getTrackbarPos('Saturation Upper', 'Trackbars')
    v_upper = cv2.getTrackbarPos('Value Upper', 'Trackbars')

    lower = (h_lower, s_lower, v_lower)
    upper = (h_upper, s_upper, v_upper)
    lower = (0,0,19)
    #upper = (179,121,206)

    mask = cv2.inRange(hsv, lower, upper)
    masked_img = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    num_objects = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        #print(area)
        if area > 400 and area < 4200: 
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect).astype('int')
            cv2.polylines(frame, [box], isClosed=True, color=(255, 0, 0), thickness=2)

            # display area
            center = (int(rect[0][0]), int(rect[0][1]))
            cv2.putText(frame,str(area), center, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
    


            num_objects += 1

    cv2.putText(frame,str(num_objects),(80,80),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,50),3)

    #cv2.imshow("Original Image", image)
    cv2.imshow("Frame", frame)
    #cv2.imshow("Mask", mask)
    #cv2.imshow("Masked Image", masked_img)


    key = cv2.waitKey()
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
