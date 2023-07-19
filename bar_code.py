import numpy as np
import cv2
from pyzbar.pyzbar import decode

def nothing(x):
    pass

cv2.namedWindow("result",cv2.WINDOW_NORMAL)
cv2.resizeWindow("result",600,600)

image = cv2.imread('data/18.jpeg')
cv2.imshow("result", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("result", gray)

# _,thresh = cv2.threshold(gray, x, y, cv2.THRESH_BINARY)
# cv2.imshow("result", thresh)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.createTrackbar('x', 'image', 0, 255, nothing)
cv2.createTrackbar('y', 'image', 0, 255, nothing)

thresh = image
while(True):
    # show image
    cv2.imshow('image', thresh)
  
    # for button pressing and changing
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
  
    # get current positions of all Three trackbars
    x = cv2.getTrackbarPos('x', 'image')
    y = cv2.getTrackbarPos('y', 'image')
    
    # display color mixture
    _,thresh = cv2.threshold(gray, x, y, cv2.THRESH_BINARY)
    kernel = np.ones((2,3), np.uint8)
    # dilate = cv2.erode(thresh,kernel,iterations=2)
    cv2.imshow("result", thresh)


cv2.waitKey(1000)
cv2.destroyAllWindows()