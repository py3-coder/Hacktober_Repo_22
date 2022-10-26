import cv2
from deepface import DeepFace
import numpy as np
import os

face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'  #getting a haarcascade xml file

face_cascade = cv2.CascadeClassifier(face_cascade_name)  #processing it for our project

if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):  #adding a fallback event
    print("Error loading xml file")


cap=cv2.VideoCapture("Input1.mp4")  #requesting the input from the video file

# Properties
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)

# Video Writer 
video_writer = cv2.VideoWriter(os.path.join('Output1.MP4'), cv2.VideoWriter_fourcc('P','I','M','1'), fps, (width, height))



# Loop through each frame
for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    _,frame = cap.read()


    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #changing the video to grayscale to make the face analysis work properly
    face=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)


    for x,y,w,h in face:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)  #making a recentangle to show up and detect the face and setting it position and colour


    #making a try and except condition in case of any errors
    try:
        analyze = DeepFace.analyze(frame, enforce_detection= False, actions=['emotion'])  #same thing is happing here as the previous example, we are using the analyze class from deepface and using ‘frame’ as input
        print(analyze['dominant_emotion'])  #here we will only go print out the dominant emotion also explained in the previous example
    except:
        print("no face")

    font = cv2.FONT_HERSHEY_SIMPLEX

    #Inserting text on video
    cv2.putText(frame, analyze['dominant_emotion'], (0, 40), font, 2, (20, 82 ,238), 5, cv2.LINE_4)

    #this is the part where we display the output to the user
    cv2.imshow('video', frame)

    # Write out frame 
    video_writer.write(frame)

    key=cv2.waitKey(1) 
    if key & 0xFF==ord('q'):   # here we are specifying the key which will stop the loop and stop all the processes going
        break
        
cap.release()
cv2.destroyAllWindows()

# Release video writer
video_writer.release()