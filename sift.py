import cv2
import numpy as np

img = cv2.imread('crop1.jpg')
img = cv2.resize(img, (0,0), fx=0.12, fy=0.12)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)

#img=cv2.drawKeypoints(gray,kp, None)
img2 = None
img2=cv2.drawKeypoints(gray,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('sift', img2)
cv2.waitKey(0)