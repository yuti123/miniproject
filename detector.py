import cv2,os
import numpy as np
from PIL import Image 
import pickle
import sqlite3

font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'

def getdata(id):
    conn=sqlite3.connect("face.db")
    cmd="SELECT * FROM PERSON WHERE id='"+str(id) +"'"
    cursor=conn.execute(cmd)
    proflie=None
    for row in cursor:
        #print row
        proflie=row
    conn.close()
    print proflie
    return proflie

   

cam = cv2.VideoCapture(0)
# font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) #Creates a font
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        int(id)

        proflie=getdata(id)
        if (proflie!= None):
            cv2.putText(im,str(proflie[0]), (x,y+h+20),font, 1,255,2,cv2.LINE_AA)
            cv2.putText(im,str(proflie[1]), (x,y+h+45),font, 1,255,2,cv2.LINE_AA)
            cv2.putText(im,str(proflie[2]), (x,y+h+65),font, 1,255,2,cv2.LINE_AA)
            cv2.putText(im,str(proflie[3]), (x,y+h+85),font, 1,255,2,cv2.LINE_AA)
            cv2.putText(im,str(proflie[4]), (x,y+h+110),font, 1,255,2,cv2.LINE_AA)


        # if(id==0):
        #      id='unknown'
        # elif(id==1):
        #      id='Ankit'
        # elif(id==2):
        #      id='Chetna'
        # elif(id==3):
        #      id='Yuti'

        # elif(id==4):
        #      id='Monali'

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

        # cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

        print(id)
        cv2.imshow('im',im)
        cv2.waitKey(10)









