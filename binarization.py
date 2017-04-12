# coding:utf-8
import cv2
import numpy as np
import matplotlib

#img = cv2.imread('./Lenna.bmp') # 画像の読み込み
img = cv2.imread('./Parrots.bmp') # 画像の読み込み
#print(img) # タプル

# GLAYスケールにする
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# thresholdメソッド
# cv2.threshold(img_src,thresh(閾値),画素値の最大,２値化するタイプ)
thresh = 100
max_pix = 255

ret, img = cv2.threshold(img_gray,thresh,max_pix,cv2.THRESH_BINARY)

#cv2.imwrite('binarization.bmp', img) # BMP形式で保存
cv2.imshow('result', img) # 表示する
cv2.waitKey(0)
cv2.destroyAllWindows() # 表示を終了する

