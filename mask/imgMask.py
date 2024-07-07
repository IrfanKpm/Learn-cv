import cv2
import numpy as np

# Load the image
frame = cv2.imread("screen100.png")

h,w,_ = frame.shape
n = 3
frame = cv2.resize(frame, (int(w/n), int(h/n)))
# Create a window to display trackbars
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
     # Convert the frame to HSV color space
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

    mask = cv2.inRange(hsv, lower, upper)

    masked_img = cv2.bitwise_and(frame, frame, mask=mask)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        cv2.drawContours(frame, [contour], 0, (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Masked Image", masked_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
