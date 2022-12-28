import cv2 as cv

cap = cv.VideoCapture('http://192.168.1.91:8080/video')

while True:
    ret, frame = cap.read()
    frame = cv.resize(frame, (0, 0), fx=0.4, fy=0.4)
    frame = cv.rotate(frame, cv.ROTATE_90_COUNTERCLOCKWISE)
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()