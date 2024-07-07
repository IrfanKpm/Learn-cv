import cv2
import mediapipe as mp

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh


# Start capturing video from the webcam
video_capture = cv2.VideoCapture(0)

# Initialize MediaPipe Face Mesh
with mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) as face_mesh:
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect face landmarks in the frame
        results = face_mesh.process(frame_rgb)
        h,w,_ = frame.shape
        # If face landmarks are detected, mark them
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for landmark in face_landmarks.landmark:
                    x = int(landmark.x * w)
                    y = int(landmark.y * h)
            # Draw a circle around the landmark point
                    cv2.circle(frame, (x, y), radius=1, color=(0, 255, 0), thickness=-1)
        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture object
video_capture.release()
cv2.destroyAllWindows()
