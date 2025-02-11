vdo = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = vdo.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video Original', frame)
    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break