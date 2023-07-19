import cv2
import numpy as np
from pyzbar.pyzbar import decode

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)
    print(barcode)
    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)
        
        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        
        cv2.putText(img, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        print("Barcode: "+barcodeData +" | Type: "+barcodeType)

cv2.namedWindow("Result",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Result", 600, 600)

img = cv2.imread("data/11.jpeg")
decoder(img)
cv2.imshow("Result", img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# cap = cv2.VideoCapture('data/vid8.mp4')
# while True:
#     ret, img = cap.read()
#     decoder(img)
#     cv2.imshow('Image', img)
#     code = cv2.waitKey(10)
#     if code == ord('q'):
#         break