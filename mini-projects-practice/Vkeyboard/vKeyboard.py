import cv2
import mediapipe as mp
import math
import time 


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

def disx(pt1,pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 3)


msg = ''
cooldown_period = 0.8
last_click_time = time.time()



def BBtn(frame, top_left, length, breadth,text, alpha=0.5,color=(138, 11, 246)):
    bottom_right = (top_left[0] + length, top_left[1] + breadth)
    b, g, r = color
    color_with_alpha = (b, g, r, int(alpha * 255))
    overlay = frame.copy()
    cv2.rectangle(overlay, top_left, bottom_right, color_with_alpha, -1)
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 4
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = top_left[0] + (length - text_size[0]) // 2
    text_y = top_left[1] + breadth // 2 + text_size[1] // 2
    #cv2.circle(frame,(text_x,text_y),3,(255,255,255),2,-1)
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, (0, 255, 0), thickness) 

def KeyboardBtn(frame):
    BBtn(frame, (50,300), 60,60,'Q')
    BBtn(frame,(120,300),60,60,'W')
    BBtn(frame,(190,300),60,60,'E')
    BBtn(frame,(260,300),60,60,'R')
    BBtn(frame,(330,300),60,60,'T')
    BBtn(frame,(400,300),60,60,'Y')
    BBtn(frame,(470,300),60,60,'U')
    BBtn(frame,(540,300),60,60,'I')
    BBtn(frame,(610,300),60,60,'O')
    BBtn(frame,(690,300),60,60,'P')
    ############################
    BBtn(frame,(80,370), 60,60, 'A')
    BBtn(frame,(150,370),60,60,'S')
    BBtn(frame,(220,370),60,60,'D')
    BBtn(frame,(290,370),60,60,'F')
    BBtn(frame,(360,370),60,60,'G')
    BBtn(frame,(430,370),60,60,'H')
    BBtn(frame,(500,370),60,60,'J')
    BBtn(frame,(570,370),60,60,'K')
    BBtn(frame,(640,370),60,60,'L')
    ############################
    BBtn(frame,(140,440),60,60,'Z')
    BBtn(frame,(220,440),60,60,'X')
    BBtn(frame,(290,440),60,60,'C')
    BBtn(frame,(360,440),60,60,'V')
    BBtn(frame,(430,440),60,60,'B')
    BBtn(frame,(500,440),60,60,'N')
    BBtn(frame,(570,440),60,60,'M')
    ##############################
    BBtn(frame,(50,235),210,50,'clear')
    BBtn(frame,(280,235),210,50,'tab')
    BBtn(frame,(510,235),210,50,'<-')



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
    cv2.putText(frame,msg, (150, 180), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 4)
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
                 if 50 < x < 110 and 300 < y < 360:
                    msg += "Q"
                 elif 120 < x < 180 and 300 < y < 360:
                    msg += "W"
                 elif 190 < x < 250 and 300 < y < 360:
                    msg += "E"
                 elif 260 < x < 320 and 300 < y < 360:
                    msg += "R"
                 elif 330 < x < 390 and 300 < y < 360:
                    msg += "T"
                 elif 400 < x < 460 and 300 < y < 360:
                    msg += "Y"
                 elif 470 < x < 530 and 300 < y < 360:
                    msg += "U"
                 elif 540 < x < 600 and 300 < y < 360:
                    msg += "I"
                 elif 610 < x < 670 and 300 < y < 360:
                    msg += "O"
                 elif 690 < x < 750 and 300 < y < 360:
                    msg += "P"
                 elif 80 < x < 140 and 370 < y < 430:
                     msg += "A"
                 elif 150 < x < 210 and 370 < y < 430:
                     msg += "S"
                 elif 220 < x < 280 and 370 < y < 430:
                     msg += "D"
                 elif 290 < x < 350 and 370 < y < 430:
                     msg += "F"
                 elif 360 < x < 420 and 370 < y < 430:
                     msg += "G"
                 elif 430 < x < 490 and 370 < y < 430:
                     msg += "H"
                 elif 500 < x < 560 and 370 < y < 430:
                     msg += "J"
                 elif 570 < x < 630 and 370 < y < 430:
                     msg += "K"
                 elif 640 < x < 700 and 370 < y < 430:
                     msg += "L"
                 elif 140 < x < 200 and 440 < y < 500:
                     msg += "Z"
                 elif 220 < x < 280 and 440 < y < 500:
                     msg += "X"
                 elif 290 < x < 350 and 440 < y < 500:
                     msg += "C"
                 elif 360 < x < 420 and 440 < y < 500:
                     msg += "V"
                 elif 430 < x < 490 and 235 < y < 500:
                     msg += "B"
                 elif 500 < x < 560 and 440 < y < 500:
                     msg += "N"
                 elif 570 < x < 630 and 440 < y < 500:
                     msg += "M"
                 elif 50 < x < 260 and 235 < y < 285:
                    msg = ''
                 elif 280 < x < 490 and 235 < y < 285:
                     msg += " "
                 elif 510 < x < 720 and 235 < y < 285:
                     msg = msg[:-1]

    KeyboardBtn(frame)
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break

cap.release()
cv2.destroyAllWindows()
