import numpy as np
import cv2

# Change matrix 'a' and 'b'
a = np.full((3, 3), 150)
b = np.full((3, 3), 100)

# Compute A - B
a_minus_b = a - b

# Compute A + B and A * B
a_plus_b = a + b
a_times_b = a * b

# Convert matrices to 8-bit unsigned integer images
a_img = np.uint8(a)
b_img = np.uint8(b)
a_plus_b_img = np.uint8(a_plus_b)
a_times_b_img = np.uint8(a_times_b)
a_minus_b_img = np.uint8(a_minus_b)

# Resize matrices to 300x300 pixels
a_img_resized = cv2.resize(a_img, (300, 300))
b_img_resized = cv2.resize(b_img, (300, 300))
a_plus_b_img_resized = cv2.resize(a_plus_b_img, (300, 300))
a_times_b_img_resized = cv2.resize(a_times_b_img, (300, 300))
a_minus_b_img_resized = cv2.resize(a_minus_b_img, (300, 300))

# Display resized matrices in different frames using OpenCV
cv2.imshow('Matrix A', a_img_resized)
cv2.imshow('Matrix B', b_img_resized)
cv2.imshow('Matrix A + B', a_plus_b_img_resized)
cv2.imshow('Matrix A * B', a_times_b_img_resized)
cv2.imshow('Matrix A - B', a_minus_b_img_resized)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
