import streamlit as st
import streamlit.components.v1 as components
import cv2
import logging as log
import datetime as dt
from time import sleep

# To learn about haar cascade : https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html
# to learn more about Streamlit : https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

# Streamlit begins

# Title
st.title("Face Detection Through Opencv Using Streamlit")
st.header("Streamlit")




# Building a sidebar
st.sidebar.subheader("Details of the person")
t1 = st.sidebar.text_input("Name of the Person 1")
s1 = st.sidebar.text_input("Age of the person 1")



st.sidebar.subheader("Details of the person")
t2 = st.sidebar.text_input("Name of the Person 2")
s2 = st.sidebar.text_input("Age of the person 2")

st.write("Name: ",t1)
st.write("Age: ", s1) # taking data from the sidebar
st.write("Name: ",t2)
st.write("Age: ", s2) # taking data from the sidebar

# Some other functions.
# st.map()
# st.radio
# st.checkbox
# st.pyplot
# st.images



# Accessign haar files: https://github.com/opencv/opencv/tree/master/data/haarcascades
components.html('<html><body>Note: The haar cascade files can be downloaded from the '
            '<a href = "https://github.com/opencv/opencv/tree/master/data/haarcascades">'
            'OpenCV Github repository</a></body></html>')



st.header("Les gooo")
if st.button("lets detect your face ?"):
    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        if anterior != len(faces):
            anterior = len(faces)
            log.info("faces: " + str(len(faces)) + " at " + str(dt.datetime.now()))

        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Display the resulting frame
        cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()