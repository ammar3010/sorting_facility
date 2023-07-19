from ultralytics import YOLO
import numpy
import cv2

model = YOLO(model="models/best.pt")

vid_path = "data/vid2.mp4"
cap = cv2.VideoCapture(vid_path)

while cap.isOpened():
    _,frame = cap.read()
    
    if _:
        results = model(frame)
        # print(results[0])
        
        annotated_frame = results[0].plot()
        cv2.imshow("YOLO_result", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break