import cv2
import cvzone
import json
import numpy as np

cv2.namedWindow("Parking", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Parking", 1000,700)

#cv2.namedWindow("imgMedian", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("imgMedian", 1000,700)

# width, height = 31,42

Carparking = []


cap = cv2.VideoCapture("parking.mp4")

if cap is None:
     print('Check the camera status!')



with open('Carpark.json', 'r') as f:
        totalPos = json.load(f)


def checkparkingspace(imgPro):

      spotCount = 0

      for pos in totalPos:
        car_values = list(pos.values())[0]

        mask = np.zeros(imgPro.shape[:2], np.uint8)
        
        cv2.fillPoly(mask, [np.array(car_values)], 255)
       
        imgcrop = cv2.bitwise_and(imgPro, mask)

        #cv2.imshow(str(x*y), imgcrop)
        count = cv2.countNonZero(imgcrop)

        x,y = car_values[0]
        cvzone.putTextRect(img, str(count), (x+80, y), scale=2.0, thickness=2, offset=0) #Pixel values display
        
        if count > 1200:
            color = (0,0,255)
            thickness = 5
            spotCount += 1
             
        else:
            color = (0,255,0)
            thickness = 7

        
        cv2.polylines(img, [np.array(car_values)],True, color, thickness) 

        # Vacant / Occupied Display
      cvzone.putTextRect(img, f"Vacant:- {len(totalPos)-spotCount}/{len(totalPos)}", (500,200), 
                         scale=5.0, thickness=3, offset=0, colorR=(0,220,0))



while True:


    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3,3), 1)
    imgPro = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)

    imgMedian = cv2.medianBlur(imgPro, 5)
    kernel = np.ones((3,3), np.int8)
    imgdilate = cv2.dilate(imgMedian, kernel, iterations=1)



    checkparkingspace(imgdilate)
         

    cv2.imshow("Parking", img)
    # cv2.imshow("imgMedian", imgMedian)
    cv2.waitKey(1)


cap.release()
cv2.destroyAllWindows()
     