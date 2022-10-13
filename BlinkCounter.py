import cv2

import cvzone

from cvzone.FaceMeshModule import FaceMeshDetector

cap =cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
##list for detecting eye
idList=[22,23,24,26,110,157,158,159,160,161,130,243]

##to check if video is present
if(cap.isOpened()==False):
    print("error while opening the video")
    exit()
##the segment to display the video already stored in  the system
while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES)==cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)


    ##reading the image

    success, img = cap.read()

    #detecting face

    img,faces=detector.findFaceMesh(img,draw=False)
    if faces:
        face=faces[0]
        for id in idList:
            cv2.circle(img,face[id],2,(255,0,255),cv2.FILLED)
        ##to find the distance between top eyelid and bottom eyelid
        leftUp=face[159]
        leftDown=face[23]
        leftLeft=face[130]
        leftRight=face[243]

        lengthVer,_  =detector.findDistance(leftUp,leftDown)
        lengthHor,_=detector.findDistance(leftLeft,leftRight)

        cv2.line(img,leftUp,leftDown,(0,200,0),3)
        cv2.line(img,leftLeft,leftRight,(0,200,0),3)

        print(lengthVer)
        print(lengthHor)
    img=cv2.resize(img,(1280,720))

    cv2.imshow("kando mona video",img)
    cv2.waitKey(1)
