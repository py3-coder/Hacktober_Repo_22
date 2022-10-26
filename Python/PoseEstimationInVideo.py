import cv2
import mediapipe as mp
import os

mpDraw=mp.solutions.drawing_utils  
mpPose=mp.solutions.pose          #Creating object to detect pose
pose=mpPose.Pose()

cap = cv2.VideoCapture(os.path.join("Video 2.mp4"))    #Requesting the input from the video file

# Properties
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)

# Video Writer 
video_writer = cv2.VideoWriter(os.path.join('Output2.MP4'), cv2.VideoWriter_fourcc('P','I','M','1'), fps, (width, height))

# Loop through each frame
for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    _,frame = cap.read() 
    frameRGB= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  #converting image to RGB because "mediapipe" use RGB format

    results= pose.process(frameRGB)  #Sending image to model
    print(results.pose_landmarks)

    if results.pose_landmarks:     #Checking if the landmark is detected or not and then drawing the landmarks
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)


    cv2.imshow("Video", frame)  #Displaying the output to user

    # Write out frame 
    video_writer.write(frame)

    key=cv2.waitKey(1) 
    if key & 0xFF==ord('q'):   # here we are specifying the key which will stop the loop and stop all the processes going
        break
        
cap.release()
cv2.destroyAllWindows()

# Release video writer
video_writer.release()