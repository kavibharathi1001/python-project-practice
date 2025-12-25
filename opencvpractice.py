import cv2 as cv
video =cv.VideoCapture(0)
while True:
    ret,frame=video.read()

    # gray =cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # cv.imshow("Frame",gray)
    cv.imshow("Frame2",frame)
    cv.waitKey(1)
video.release()
cv2.destroyAllWindows(1)