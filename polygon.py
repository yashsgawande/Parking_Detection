import cv2
import numpy as np
import json
import os



img = cv2.imread("carParkImg.png")

if img is None:
    print('Check the carParking.png status!')


Carparking = []
slot_id = 1

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Image", 1000,700)

#width, height = 31,42


poslist = []
slots = {}

# This checks if the Carparking.json file is exists then it took the polygon from that...

try:
     with open('Carpark.json', 'r') as f:
         Carparking = json.load(f)

     for car in Carparking:
        car_values = list(car.values())[0]
        cv2.polylines(img, [np.array(car_values)], True, (0, 255, 0), 5)

except:

    Carparking = []


# Mouse clicks are here to draw the parking polygon...

def mouseclick(event,x,y,flag,param):
    global Carparking
    global slot_id
    global slots
    
    # When the 4 mouse click was happen it draws the polygon and saves it to the Carparking.json

    if event == cv2.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
        if len(poslist) == 4:
            print("Polygon is Formed!")
            cv2.polylines(img, [np.array(poslist)], True, (0, 255, 0), 5)

            with open('Carpark.json', 'w') as f:
                slots = {slot_id : poslist.copy()}
                Carparking.append(slots)
                json.dump(Carparking, f, indent=4)
                poslist.clear()
                slot_id += 1


while True:

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseclick)
    cv2.waitKey(1)

