import cv2

cap = cv2.VideoCapture("parking.mp4")

cv2.namedWindow("Parking lot", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Parking lot", 1000,700)


while True:

    success, frame = cap.read()

    if not success:
        print("Check the camera status!")
        break



    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        print("Image is Captured and saved as a carParkimg.png")
        cv2.imwrite("carParkimg.png", frame)

    elif key == 27:
        break

    cv2.imshow("Parking lot", frame)

cap.release()
cv2.destroyAllWindows()