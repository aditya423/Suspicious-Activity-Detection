import cv2 
import os 

vid = cv2.VideoCapture(r"C:\Users\Aditya\suspicious_activity_detection\project\dataset\fights\newfi1.avi")
currentframe = 0

if not os.path.exists('frames'):
    os.makedirs('frames')

while(vid.isOpened()):
    success, frame = vid.read()
    cv2.imshow('output', frame)
    cv2.imwrite('./project/dataset/fights/frames/frame' + str(currentframe) + '.jpg', frame)
    currentframe += 1
    if(cv2.waitKey(1) & 0xFF==('q')):
        break 

vid.release()
cv2.destroyAllWindows()