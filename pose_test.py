import cv2
import mediapipe as mp
count=0
flag=1
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
camera = cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:
    while camera.isOpened():
        success, image = camera.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.pose_landmarks:
            # landmarks_all=results.pose_landmarks[0].landmark
            landmarks_all=results.pose_landmarks.landmark
            y=landmarks_all[0].y
            nose_y=(y*480)
            y1=landmarks_all[16].y
            hand_y=(y1*480)
            if hand_y < nose_y and flag==1:
                count=count+1
                print(count)
                flag=0
                cv2.putText(image,'count='+str(count),(200,200),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
            elif hand_y > nose_y and flag==0:
                flag=1
        mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS,landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        cv2.imshow('MediaPipe Pose',image)
        end=cv2.waitKey(1)
        if end==ord('q'):
            break
camera.release()