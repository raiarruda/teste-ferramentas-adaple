import cv2,time

#1 crea um objeto. 
video =cv2.VideoCapture(0)
a=0
while True:


    a = a + 1
    #3
    check, frame = video.read()

    print(check)
    print(frame)
    #6
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #4
    cv2.imshow("capturing", frame)

    #5
    #cv2.waitKey(0)

    #7
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

print(a)

#2 desligara  camera
video.release()

cv2.destroyAllWindows