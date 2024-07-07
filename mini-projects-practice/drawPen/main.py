import cv2
import mediapipe as mp
import math


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
max_num_hands = 1
min_detection_confidence = 0.5  
min_tracking_confidence = 0.5 
hands = mp_hands.Hands(
    max_num_hands=max_num_hands,
    min_detection_confidence=min_detection_confidence,
    min_tracking_confidence=min_tracking_confidence
)

def disx(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 3)




# Initialize arrays to store data points
data_x = []
data_y = []

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        print("Error: Couldn't read frame.")
        break
    height, width, _ = frame.shape
    h = int(height * 1.2)
    w = int(width * 1.2)
    frame = cv2.resize(frame, (w, h))
    rgb = image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            points = []
            for idx, landmark in enumerate(hand_landmarks.landmark):
                if idx == 8:
                    cx8, cy8 = int(landmark.x * w), int(landmark.y * h)
                    cv2.circle(frame, (cx8, cy8), 6, (255, 0, 0), -1)
                    points.append((cx8, cy8))
                if idx == 4:
                    cx4, cy4 = int(landmark.x * w), int(landmark.y * h)
                    cv2.circle(frame, (cx4, cy4), 6, (255, 0, 0), -1)
                    points.append((cx4, cy4))

            if len(points) == 2:
                cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
                midpoint = ((points[0][0] + points[1][0]) // 2, (points[0][1] + points[1][1]) // 2)
                cv2.circle(frame, midpoint, 6, (0, 0, 180), -1)
                dis = disx(points[0], midpoint)
                if dis < 25:
                    x = midpoint[0]
                    y = midpoint[1]
                    cv2.circle(frame, (x, y), 6, (0, 0, 255), -1) 

                    # Add new data points to arrays
                    data_x.append(x)
                    data_y.append(y)

                    # Check if length exceeds 400
                    if len(data_x) > 400:
                        data_x.pop(0)  # Remove oldest data point
                        data_y.pop(0)

    # Draw lines between consecutive points
    for (x1, y1), (x2, y2) in zip(zip(data_x, data_y), zip(data_x[1:], data_y[1:])):
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 4)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
