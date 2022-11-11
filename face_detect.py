import cv2
import mediapipe as mp
import winsound
frequency=2000
duration=500
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
camera = cv2.VideoCapture(1)
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    while camera.isOpened():
        success, image = camera.read()
        if not success:
            print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
            continue
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.detections:
            for detection in results.detections:
                score=detection.score[0]
                if score >0.8:
                    mp_drawing.draw_detection(image, detection)
                    cv2.putText(image,str(detection.score[0]),(100,200),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
                else:
                    cv2.putText(image,'unknown face detected',(100,200),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
                    winsound.Beep(frequency,duration)
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Face Detection', image)
        end=cv2.waitKey(1)
        if end==ord('q'):
            break
camera.release()