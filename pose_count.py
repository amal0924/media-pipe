import streamlit
import cv2
import pose_sub
streamlit.title('hello world')
start_button=streamlit.button('START')
image_placeholder=streamlit.empty()
camera=cv2.VideoCapture(0)
if start_button:
    while True:
        live_video,count=pose_sub.hand_count(camera)
        image_placeholder.image(live_video,width=500)
        if count>=10:
            results=count*0.33  #(0.33 is the calorie burned while raising hand one time)
            streamlit.text('task completed and calories burned='+str(results))
            camera.release()
            image_placeholder.empty()
            break