import cv2 as cv

# Reading images for openCV
img = cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat', img)

# Reading videos for openCV

vdo = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = vdo.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

vdo.release()
cv.destroyAllWindows()


cv.waitKey(0)