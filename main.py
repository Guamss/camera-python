import os
import cv2

def change_res(capture, width, height):
    w =capture.set(3, width)
    h =capture.set(4, height)
    return w, h

fps = 24.0
capture = cv2.VideoCapture(0)
dimension = change_res(capture, 640, 480) #480p
out = cv2.VideoWriter('video1.mp4', cv2.VideoWriter_fourcc(*"XVID"), fps, (640, 480))

while True:
    ret, frame = capture.read()
    if ret==True:
        out.write(frame)
        cv2.imshow("camera", frame)
        if cv2.waitKey(100) == ord("q"):
            break 
    else:
        break

path = "/Your path/camera-python/video"
os.system(f"/Your path/camera-python/video1.mp4 {path} && mv {path}video1.mp4 {path}$(date +%F-%H:%M).mp4")
capture.release()
cv2.destroyAllWindows()


