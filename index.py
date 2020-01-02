# 画像のサイズを変更する
# グリッド線を引く
# 各マス目の色を取得
# colorCodeに変換

import cv2
import numpy as np

fname = "input.jpg"
img = cv2.imread(fname)

# 高さを150,幅を300に変更する
hight = 300
wight = 150
newImg = cv2.resize(img, (hight, wight))

# [補足]画像に区切りをつける
## 画像のy軸,x軸を取得
yImg,xImg = newImg.shape[:2]
## y軸とx軸の線を引く間隔を指定
yStep,xStep = 50,50
## 横線を引く：y_stepからimg_yの手前までy_stepおきに茶色(BGRが48,80,116)横線を引く
## 縦線を引く：x_stepからimg_xの手前までx_stepおきに茶色(BGRが48,80,116)縦線を引く
newImg[yStep:yImg:yStep, :, :] = 48,80,116
newImg[:, xStep:xImg:xStep, :] = 48,80,116

# 保存
cv2.imwrite('output.png',newImg)

# 新しくできたファイルを読み込み
img = cv2.imread('output.png')

# 画像の場所によってBGRを取得する
y = 25
x = 25
for i in range (y, 150, 50):
	for j in range (x, 300, 50):
		# GBRを取得
		color = img[i, j]
		# colorCode(R,G,Bの順)に変換
		color_code = '#%02X%02X%02X' % (color[2],color[1],color[0])

		# [todo]color_codeを料理