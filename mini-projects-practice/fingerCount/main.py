import cv2
import mediapipe as mp
import math
import time 


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
# Drawing specifications
drawLandmark = mp.solutions.drawing_utils
landmark_spec = drawLandmark.DrawingSpec(color=(200, 0, 0), thickness=2, circle_radius=3)
connection_spec = drawLandmark.DrawingSpec(color=(0, 0, 180), thickness=2)



def LandMarkDraw(frame):
    drawLandmark.draw_landmarks(frame, hand_landmarks, 
                                      mp_hands.HAND_CONNECTIONS,
                                      landmark_drawing_spec=landmark_spec,
                                      connection_drawing_spec=connection_spec
                                      )






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
    ############################
    count = 0
    ############################
    if results.multi_hand_landmarks:
       for hand_landmarks in results.multi_hand_landmarks:
        points = {
           4 : 0,
           5:0,
           6 : 0,
           8 : 0,
           10 : 0,
           12 : 0,
           14 : 0,
           16 : 0,
           18 : 0,
           20 : 0,
        }
        for idx, landmark in enumerate(hand_landmarks.landmark):
            if idx in points:
                cx,cy = int(landmark.x * w),int(landmark.y * h)
                points[idx] = (cx,cy)
        if points[8][1] < points[6][1]:      
           count+=1
           cv2.line(frame,(points[8][0],points[8][1]),(points[6][0],points[6][1]),(0,255,0),3)
        if points[12][1] < points[10][1]:
           count+=1 
           cv2.line(frame,(points[12][0],points[12][1]),(points[10][0],points[10][1]),(0,255,0),3)
        if points[16][1] < points[14][1]:
           count+=1
           cv2.line(frame,(points[16][0],points[16][1]),(points[14][0],points[14][1]),(0,255,0),3)
        if points[20][1] < points[18][1]:
           count+=1
           cv2.line(frame,(points[20][0],points[20][1]),(points[18][0],points[18][1]),(0,255,0),3)
        if points[4][0] < points[5][0]:
           count+=1
           cv2.line(frame,(points[4][0],points[4][1]),(points[5][0],points[5][1]),(0,255,0),3)
    cv2.putText(frame,str(count), (600, 180), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 200, 0), 8)

    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break

cap.release()
cv2.destroyAllWindows()
