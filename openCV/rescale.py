import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('IMAGE', img)

def rescaleFrame(frame, scale=0.2):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Only for Live Videos
    vdo.set(3, width)
    vdo.set(4, height)

resized_image = rescaleFrame(img)



vdo = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = vdo.read()
    frame_resized = rescaleFrame(frame)

    # cv.imshow('Video Original', frame)
    # cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cv.waitKey(0)