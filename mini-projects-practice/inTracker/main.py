import cv2
import math


cap = cv2.VideoCapture(0)


#tracker = cv2.legacy.TrackerMOSSE_create()
tracker = cv2.TrackerCSRT_create()

status,frame = cap.read()
frame = cv2.flip(frame,1)
cv2.putText(frame,"Select Target",(60, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
bbox = cv2.selectROI("Target Frame",frame,False)
tracker.init(frame,bbox)
cv2.destroyWindow('Target Frame')
def DrawBox(frame,bbox):
    x,y,length,breadth = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    mid_x = int(x+length/2)
    mid_y = int(y+breadth/2)
    cv2.circle(frame,(mid_x,mid_y),3,(0,0,255),-1)
    cv2.putText(frame,"Target Locked",(40, 90),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame,"Tracking",(40, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.rectangle(frame,(x,y),(x+length,y+breadth),(255,0, 255),6)

    h, w, _ = frame.shape
    center_x = w // 2
    center_y = h // 2
    cv2.line(frame, (0, center_y), (w, center_y), (0, 255, 0), 2)
    cv2.line(frame, (center_x, 0), (center_x, h), (0, 255, 0), 2)

    disx = mid_x - center_x
    disy = (mid_y - center_y)*-1

    angle_rad = math.atan2(disy, disx)
    angle_deg = math.degrees(angle_rad)
    angle_deg %= 360


    cv2.putText(frame,f"x -> {disx}",(370, 50),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),2)
    cv2.putText(frame,f"y -> {disy}",(370, 75),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),2) 
    cv2.putText(frame,f"angle -> {angle_deg:.1f}",(370, 100),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 255, 0),2)   

  

while cap.isOpened():
    status,frame = cap.read()
    frame = cv2.flip(frame,1)
    state,bbox = tracker.update(frame)
    #print(bbox)
    if state:
        DrawBox(frame,bbox)
    else:
        cv2.putText(frame,"Lose",(40,130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()