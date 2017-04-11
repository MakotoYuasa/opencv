#coding:utf-8
import cv2

capture = cv2.VideoCapture(0)

while(True):
    ret, frame = capture.read()

    # フレームの表示
    cv2.imshow('camera', frame)

    k = cv2.waitKey(1) # 1msec待つ
    if(k == 27 || k == ord('q')): # ESCキーまたはqキーが入力された場合
        break
    elif(k == ord('s')): # sキーを押された場合
       cv2.imwrite('picture.png', frame)

capture.release()
cv2.destroyAllWindows() # ウインドウを閉じる
