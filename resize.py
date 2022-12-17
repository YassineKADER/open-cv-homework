import cv2 as cv


#a simple resize function
def rescaleFrame(frame, scale=0.75):
    #work for videos, images, live videos
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    print(frame.shape)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


#resize an image
img = cv.imread('photos/cat.jpg')
#cv.imshow('img', img)
cv.imshow('img resized', rescaleFrame(img, 0.3))
cv.waitKey(2000)

#resize a video
vid_Capture = cv.VideoCapture('videos/cat.mp4')
istrue=True
while istrue:
    istrue, frame = vid_Capture.read();#the .read() method read return a bool and the frame
    frame_resize = rescaleFrame(frame, 0.4)
    cv.imshow('video normale', frame);
    cv.imshow('video', frame_resize);
    if cv.waitKey(2) & 0xFF==ord('d'):#cv.waitKey() can be control the framereate here
        break
vid_Capture.release()
cv.destroyAllWindows()