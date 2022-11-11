import cv2
import mediapipe as mp
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
            #print(landmarks_all[1].z)
            z=landmarks_all[1].z
            z=(z*-100)
            print(z)
            if z>=8:
                cv2.putText(image,'please move back',(50,100),cv2.FONT_HERSHEY_DUPLEX,1,(255,0,0),2)
            x=landmarks_all[1].x
            x=x*640 #((x/640)*x=x  _value to get the value of certain x we multiply it by the same height640=x)
            y=landmarks_all[1].y
            y=y*480 #((y/480)*y=y  _value to get the value of certain y we multiply it by the same width480=y)
            print(x,y)
            print(image.shape)
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_TESSELATION,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
                mp_drawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_CONTOURS,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
                mp_drawing.draw_landmarks(image=image,landmark_list=face_landmarks,connections=mp_face_mesh.FACEMESH_IRISES,landmark_drawing_spec=None,connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style())
            cv2.putText(image,'x='+str(int(x))+'y='+str(int(y)),(int(x),int(y)),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0),1)
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Face Mesh',image)
        end=cv2.waitKey(1)
        if end==ord('q'):
            break
camera.release()