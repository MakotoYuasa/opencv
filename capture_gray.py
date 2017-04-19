#coding:utf-8
import cv2
import pyaudio
import wave

capture = cv2.VideoCapture(0)

# 音を出す関数
def sound():
    # wavファイルを読み込む
    wf = wave.open("sample.wav", "r")

    # ストリーム開始
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)

    data = wf.readframes(1024)
    while(data != ''):
        stream.write(data)
        data = wf.readframes(1024)

    # ストリーム終了
    stream.close()
    p.terminate()


while(True):
    ret, frame = capture.read()

    # フレームの表示
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # grayスケール化する
    cv2.imshow('gray', gray_frame)

    k = cv2.waitKey(1) # 1msec待つ
    if(k == 27 or k == ord('q')): # ESCキーまたはqキーが入力された場合
        break
    elif(k == ord('s')): # sキーを押された場合
       cv2.imwrite('picture_gray.png', gray_frame) # 保存する
       sound() # 音を出す

capture.release()
cv2.destroyAllWindows() # ウインドウを閉じる
