import cv2

import cvzone

from cvzone.FaceMeshModule import FaceMeshDetector

cap =cv2.VideoCapture('video2.webm')
detector = FaceMeshDetector(maxFaces=1)

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

    img,faces=detector.findFaceMesh(img)

    img=cv2.resize(img,(640,360))
    cv2.imshow("kando mona video",img)
    cv2.waitKey(1)
