import cv2
import mediapipe as mp
import math
import time 

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

def disx(pt1,pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 3)


cooldown_period = 0.8
last_click_time = time.time()



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
    rgb = image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    if results.multi_hand_landmarks:
       for hand_landmarks in results.multi_hand_landmarks:
        points = []
        drawLandmark.draw_landmarks(frame, hand_landmarks, 
                                      mp_hands.HAND_CONNECTIONS,
                                      landmark_drawing_spec=landmark_spec,
                                      connection_drawing_spec=connection_spec
                                      )
        for idx, landmark in enumerate(hand_landmarks.landmark):
            if idx == 8:
              cx8, cy8 = int(landmark.x * w), int(landmark.y * h)
              cv2.circle(frame,(cx8,cy8),6,(255,0,0),-1)
              points.append((cx8, cy8))
            if idx == 4:
              cx4, cy4 = int(landmark.x * w), int(landmark.y * h)
              cv2.circle(frame,(cx4,cy4),6,(255,0,0),-1)
              points.append((cx4, cy4))
  
            if len(points) == 2:
             cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
             midpoint = ((points[0][0] + points[1][0]) // 2, (points[0][1] + points[1][1]) // 2)
             cv2.circle(frame,midpoint,6,(0,0,180),-1)
             dis = disx(points[0],midpoint)
             if dis < 25:
               current_time = time.time()
               if current_time - last_click_time > cooldown_period:
                 last_click_time = time.time()
                 x = midpoint[0]
                 y = midpoint[1]


    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break

cap.release()
cv2.destroyAllWindows()
