import cv2 as cv

img = cv.imread('photos/bird.jpg')


#Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('image',gray)

#Blur                     odd number
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)

#Edge cascading
canny = cv.Canny(blur, 125, 135)
cv.imshow("cascading", canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=9)
cv.imshow('dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=9)
cv.imshow("eroded",eroded)

#Resize 
resized = cv.resize(img, (500,79), interpolation= cv.INTER_AREA)#cv.iner_area better for scale down and cV.inter_cibuc for scale up the frame
cv.imshow("resized", resized)

#Cropping
cropped = img[50:200, 300:500]
cv.imshow("crroped", cropped)

cv.imshow("blur",blur)
cv.imshow("image",img)

cv.waitKey(0)