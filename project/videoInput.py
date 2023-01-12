import numpy as np
import cv2 
import os

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret==True):
        out.write(frame)
        cv2.imshow('output', frame)
        if(cv2.waitKey(1) & 0xFF==ord('q')):
            break 
    else: 
        break 

cap.release()
cv2.destroyAllWindows()