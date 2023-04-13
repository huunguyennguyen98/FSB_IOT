import face_recognition
import os, sys
import cv2
import numpy as np
import math

# Chụp hình và lưu
video=cv2.VideoCapture(0)
a=0
i=0

while True:
    a = a + 1
    check, frame = video.read()
    cv2.imshow("Capturing", frame)
    key=cv2.waitKey(1)

    if key == ord ('r'):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
        out.write(frame)
    if key == ord ('x'):
        i+=1
        name = input('Nhap ten: ')
        cv2.imwrite('face/' + name + '.jpg', frame)
        cv2.imshow("User Capture", frame)
        print('taking pictures')
    if key == ord ('q'):
        break


print(a)
video.release()
cv2.destroyAllWindows
