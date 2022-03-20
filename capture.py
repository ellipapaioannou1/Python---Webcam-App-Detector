import cv2
import time

from cv2 import cvtColor
from cv2 import COLOR_BAYER_BG2GRAY
from cv2 import COLOR_BGR2GRAY

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

a = 0
while True:
    a = a + 1
    check, frame = video.read()

    print(check)
    print(frame)

    gray= cv2.cvtColor(frame,COLOR_BGR2GRAY)

    #time.sleep(3)
    cv2.imshow("Capturing", gray)

    key =cv2.waitKey(1)
    if key==ord('q'):
     break 

print(a)



video.release()

cv2.destroyAllWindows()