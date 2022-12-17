import cv2 as cv
import numpy as np

blank = np.zeros(shape=(700,700, 3), dtype='uint8')#uint8 dtatatype for an image

#point the image a certain color
blank[:] = 0,255,89
#draw a rectangle
#                  origin  dest       color
cv.rectangle(blank,(0,0), (350,700), (25,0,0), thickness=-1)
cv.imshow('img', blank)

#draw a circle
#                 center   radius
cv.circle(blank, (259,350),40, (0,0,255), thickness=-1)

#draw a line
cv.line(blank, (100,0), (255,255), (255,255,255), thickness=3)

#write text
cv.putText(blank, "hello world", (155,79),cv.FONT_HERSHEY_PLAIN, 1.8, (255,255,255))

cv.imshow('img', blank)
cv.waitKey(2000)