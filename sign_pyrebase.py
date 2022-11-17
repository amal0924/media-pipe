import cv2
import mediapipe as mp
import hand_sign_pyrebase
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
camera = cv2.VideoCapture(0)
with mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5) as hands:
    while camera.isOpened():
        success, image = camera.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            landmarks_all=results.multi_hand_landmarks[0].landmark
            y=landmarks_all[3].y
            tip=(y*480)
            y1=landmarks_all[5].y
            index=(y1*480)
            y2=landmarks_all[8].y
            tip2=(y2*480)
            y3=landmarks_all[6].y
            index2=(y3*480)
            y4=landmarks_all[12].y
            tip3=(y4*480)
            if tip < index:
                sign='thumps up'
                hand_sign_pyrebase.pyrebase_sign(sign)
            elif tip2 and tip3 < index2:
                sign='victory'
                hand_sign_pyrebase.pyrebase_sign(sign)
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image,hand_landmarks,mp_hands.HAND_CONNECTIONS,mp_drawing_styles.get_default_hand_landmarks_style(),mp_drawing_styles.get_default_hand_connections_style())
        cv2.imshow('MediaPipe Hands',image)
        end=cv2.waitKey(1)
        if end==ord('q'):
            break
camera.release()        