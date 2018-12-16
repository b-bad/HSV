import numpy as np
import cv2

img = cv2.imread(r"C:\Users\Administrator_wzz\Desktop\before.jpg")
cv2.imshow('before', cv2.resize(img, (800, 800)))
kernel_2 = np.ones((2, 2), np.uint8)
kernel_3 = np.ones((3, 3), np.uint8)
kernel_4 = np.ones((4, 4), np.uint8)
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
Lower = np.array([0, 0, 100])
Upper = np.array([40, 200, 255])#设置颜色范围
mask = cv2.inRange(HSV, Lower, Upper)
erosion = cv2.erode(mask,kernel_4,iterations = 1)
erosion = cv2.erode(erosion,kernel_4,iterations = 1)
dilation = cv2.dilate(erosion,kernel_4,iterations = 1)
dilation = cv2.dilate(dilation,kernel_4,iterations = 1)
ret, binary = cv2.threshold(dilation, 127, 255, cv2.THRESH_BINARY)
thresh, contours, hierrchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w > img.shape[1]/10 and h > img.shape[0]/20:#过滤过小的
        print(x, y, w, h)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 6)
cv2.imshow('after', cv2.resize(img, (800, 800)))
cv2.imwrite(r'C:\Users\Administrator_wzz\Desktop\after.jpg', img)
#cv2.imshow('dst', cv2.resize(thresh, (800, 800)))
cv2.waitKey(0)
