# Basic structure

```
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    if not ret:
        print("Error: Couldn't read frame.")
        break
    height, width, _ = frame.shape
    h = int(height * 1.2)
    w = int(width * 1.2)
    frame = cv2.resize(frame, (w, h))
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break

cap.release()
cv2.destroyAllWindows()
```

# Hand_LandMarks_Detection

```
# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
max_num_hands = 2
min_detection_confidence = 0.5
min_tracking_confidence = 0.5
hands = mp_hands.Hands(
    max_num_hands=max_num_hands,
    min_detection_confidence=min_detection_confidence,
    min_tracking_confidence=min_tracking_confidence
)
# Drawing specifications
drawLandmark = mp.solutions.drawing_utils
landmark_spec = drawLandmark.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=3)
connection_spec = drawLandmark.DrawingSpec(color=(255, 255, 255), thickness=2)

image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
results = hands.process(image_rgb)
    # Draw hand landmarks on the frame
if results.multi_hand_landmarks:
   for hand_landmarks in results.multi_hand_landmarks:
      drawLandmark.draw_landmarks(frame, hand_landmarks,
                                      mp_hands.HAND_CONNECTIONS,
                                      landmark_drawing_spec=landmark_spec,
                                      connection_drawing_spec=connection_spec
                                      )
      for idx, landmark in enumerate(hand_landmarks.landmark):
              if idx == 8:
                cx, cy = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)
```

# Overlay

```
alpha = 0.5
b, g, r = color
color_with_alpha = (b, g, r, int(alpha * 255))
overlay = frame.copy()
cv2.rectangle(overlay, top_left, bottom_right, color_with_alpha, -1)
cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
```
