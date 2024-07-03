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
face_match = False

while True:
    ret, frame = videoCapture.read() #ret - Boolean returning if a frame was captured / frame - Stores the captured frame

    if ret:
        pass

    key = cv2.waitKey(1) #Waits one second for a key press and stores the value in a variable
    if key == ord("z"): #Breaks the loop if the key values is the same as the ordinal of z
        break

cv2.destroyAllWindows()

    
