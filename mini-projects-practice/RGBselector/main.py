import cv2
import numpy as np


def xpass(x):
    pass

w = np.ones((500,500,3),np.uint8)*255
cv2.namedWindow('ColorTracker')
cv2.createTrackbar('R','ColorTracker',0,255,xpass)
cv2.createTrackbar('G','ColorTracker',0,255,xpass)
cv2.createTrackbar('B','ColorTracker',0,255,xpass)
while True:
    cv2.imshow('ColorTracker',w)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    r = cv2.getTrackbarPos('R','ColorTracker')
    g = cv2.getTrackbarPos('G','ColorTracker')
    b = cv2.getTrackbarPos('B','ColorTracker')
    w[:] = [b,g,r]

cv2.destroyAllWindows()