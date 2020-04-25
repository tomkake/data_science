import numpy as np
import cv2

filepath = "./data/test.mp4"

cap = cv2.VideoCapture(filepath)
min_white = np.array([0,0,100])
max_white = np.array([180,45,255])
def green_detect(img):
    # HSV色空間に変換
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv_min = np.array([30, 64, 0])
    hsv_max = np.array([90,255,255])
    mask1 = cv2.inRange(hsv, hsv_min,hsv_max)
    
    return mask1

while (cap.isOpened()):
    ret,frame = cap.read()
    if not ret:
        continue
    #height,width,_= frame.shape
    #resize_img = cv2.resize(frame , (int(width*0.2), int(height*0.2))
    frame = cv2.resize(frame, dsize=(320, 320))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 135, 255, 0)
    hsv_detect = green_detect(frame)
    res_white = cv2.bitwise_and(frame,frame, mask= hsv_detect)
    cv2.imshow("frame",frame)
    #cv2.imshow("frame",hsv_detect)
    cv2.imshow("mask",hsv_detect)
    cv2.imshow("frame + mask",res_white)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()