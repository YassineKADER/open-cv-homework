#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 14:09:34 2022

@author: mpower
"""

import cv2 as cv

img = cv.imread('photos/cat.jpg') #read the image 
cv.imshow('title', img) #show the image
cv.waitKey(1000) #wait 1s for a ket to be pressed then destrooy the windows
cv.destroyAllWindows()


vid_Capture = cv.VideoCapture('videos/cat.mp4')
istrue=True
while istrue:
    istrue, frame = vid_Capture.read();#the .read() method read return a bool and the frame
    cv.imshow('video', frame);

    if cv.waitKey(2) & 0xFF==ord('d'):#cv.waitKey() can be control the framereate here
        break


vid_Capture.release()

cv.destroyAllWindows()

