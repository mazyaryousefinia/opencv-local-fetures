import cv2
import numpy as np

filename = 'crop1.jpg'
img = cv2.imread(filename)
img = cv2.resize(img, (0,0), fx=0.12, fy=0.12)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,5,3,0.09)

dst = cv2.dilate(dst,None)

img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()