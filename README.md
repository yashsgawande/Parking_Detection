A computer vision based parking slot detection system built using Background Subtraction method.

The system uses a video of the parking slots where we draw the polygon over every parking slot, I chose the polygon over rectangle for flexibility of the parking slot.

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

