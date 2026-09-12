A computer vision based parking slot detection system built using Background Subtraction method.

The system uses a live footage of the parking slots where we draw the polygon over every parking slot, I chose the polygon over rectangle for flexibility of the parking slot.

All of the coordinates of the parking slots, stored in a JSON file to detect it . It process each parking region individually and provides the current parking availability.


Key Features 

• Real-time detection
• Displays vacant or occupied slot
• Custom parking slot coordinates stored in JSON
• OpenCV based image processing
• Can use on live camera feed

Technologies

• Background Subtraction Method
• NumPy
• OpenCV
• JSON


Limitations

• Lighting changes can cause false detection
• Camera angle can affect detection accuracy
• Camera movement can affect slot alignment
• Obstruction can affect detection

takeimage.py :- Take image is used to take the image from the live camera for further process. (Just import the video as of the name "parkin.mp4" other wise change the name and state according to you.

polygon.py :- polygon file is used to draw the polygon over the parking slots to further detections.

Carpark.json :- Carpark is the json file where the all parking slots coordinates get stored when you create the first parking polygon it get created automatically.

detection.py :- Detection was the final file where the all detection process was done.
