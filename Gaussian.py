# coding: utf-8

import cv2
import matplotlib
import numpy as np

# 画像の読み込み
img = cv2.imread('./Lenna.bmp')

kernel = np.ones((5,5), np.float32) / 25
#dst = cv2.filter2D(img, -1, kernel)
dst2 = cv2.GaussianBlur(img, (5,5), 0)

# 画像の表示
cv2.imshow('result', dst2)

# 画像の表示
#cv2.imshow('result', img)

# キー入力で表示の終了
cv2.waitKey(0)
cv2.destroyAllWindows()
