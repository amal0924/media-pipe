import streamlit
import cv2
import drwsy_sub
streamlit.title('hello world')
start_button=streamlit.button('detect')
image_placeholder=streamlit.empty()
stop_button=streamlit.button('stop')
camera=cv2.VideoCapture(0)
if start_button:
    while True:
        live_video=drwsy_sub.drowsy_detection(camera)
        image_placeholder.image(live_video,width=500)
        if stop_button:
            camera.release()
            break
    