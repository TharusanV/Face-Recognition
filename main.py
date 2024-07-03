"""
Packages:
pip install opencv-python deepface
"""

import threading #Allows multiple tasks to run simultaneously using threads
import cv2
from deepface import DeepFace #Lightweight facial recognition and analysis library

#Define Live Camera
videoCapture = cv2.VideoCapture(0, cv2.CAP_DSHOW) #Set to zero as I only have one camera
videoCapture.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
videoCapture.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)

#Defining Variables
frameCounter = 0 #Note: We don't want to check for a match in each frame as the neural network takes longer than a second  
faceMatch = False

#Functions
def f_checkFace(p_frame):
    pass;

while True:
    ret, frame = videoCapture.read() #ret - Boolean returning if a frame was captured / frame - Stores the captured frame

    if ret:
        if frameCounter % 30 == 0:
            try:
                #Starts a new thread to run the f_checkFace function with the current frame.
                #Using threading allows the main loop to continue capturing video without waiting for the face verification process.
                threading.Thread(target=f_checkFace, args=(frame.copy(),)).start()
            except ValueError:
                pass #Required as if DeepFace doesn't recognise a face it just returns a ValueError so we catch it

        frameCounter += 1

        #Result from the Face recognition process
        if faceMatch:
            cv2.putText(frame, "Match", (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
        else:
            cv2.putText(frame, "No Match", (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)

        cv2.imshow("video", frame) #Displays the live video with the text onto the 'video' window


    #Close the program 
    key = cv2.waitKey(1) #Waits one second for a key press and stores the value in a variable
    if key == ord("z"): #Breaks the loop if the key value is the same as the ordinal of z
        break

cv2.destroyAllWindows()

    
