import cv2
import mediapipe as mp
import eyelid_movcal
import winsound
frequency=2000
duration=100
landmarks=[]
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
camera = cv2.VideoCapture(1)
with mp_face_mesh.FaceMesh(max_num_faces=1,refine_landmarks=True,min_detection_confidence=0.5,min_tracking_confidence=0.5) as face_mesh:
    while camera.isOpened():
        success, image = camera.read()
        if not success:
            print("Ignoring empty camera frame.")
            # If loading a video, use 'break' instead of 'continue'.
            continue
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)
         # Draw the face mesh annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_face_landmarks:
            landmarks_all=results.multi_face_landmarks[0].landmark
            z=landmarks_all[1].z
            z=(z*-100)
            print(z)
            if z>=7:
                cv2.putText(image,'please move back',(50,100),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
                x1=landmarks_all[159].x
                x1=x1*640 #((x/640)*x=x   to get the value of certain x we multiply it by the same height640=x)
                y1=landmarks_all[159].y
                y1=y1*480 #((y/480)*y=y   to get the value of certain y we multiply it by the same width480=y)
                x2=landmarks_all[145].x
                x2=x2*640
                y2=landmarks_all[145].y
                y2=y2*480
            # print(x1,x2,y1,y2)
                distance=eyelid_movcal.find_distance(x1,x2,y1,y2)#(function call to find euclidean distance)
                print(distance)
                if distance<5:
                    cv2.putText(image,'sleeping..pls wakeup..',(100,200),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
                    winsound.Beep(frequency,duration)
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_TESSELATION,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
                mp_drawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_CONTOURS,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
                mp_drawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_IRISES,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style())
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Face Mesh',image)
        end=cv2.waitKey(1)
        if end==ord('q'):
            break
camera.release()