import cv2
import numpy as np
import color_code

# 画像を入力
fname = "input.jpg"
img = cv2.imread(fname)

# todo:読み込んだ画像のサイズをなんとかする
## 画像の高さと幅を取得
h,w = img.shape[:2]
## 高さを600,幅を400に変更する
hight = 600
width = 400
newImg = cv2.resize(img, (width, hight))
## 保存
cv2.imwrite('output.png',newImg)

# 加工した画像を読み込み
img = cv2.imread('output.png')

# 加工した画像の座標の色によって絵文字を選定
## １マス:25×25
## ヨコ:16 タテ:24
step_y = 25
step_x = 25
y = int(step_y / 2) #12
x = int(step_x / 2) #12
nline = 16 # ドット絵の１行:ヨコ

dot = ''
count = 0
for i in range (y, hight, step_y):
	for j in range (x, width, step_x):
		count += 1
		# GBRを取得
		color = img[i, j]
		# colorCodeを変換
		dot += str(color_code.make_dot(color[2], color[1], color[0]))
		# 改行処理
		if count % nline == 0:
			dot += '\n'

print (dot)