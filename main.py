import cv2
import sys
import numpy as np
import color_code
import img_edit

# 画像を入力
fname = "img/input.jpg"
img = cv2.imread(fname)

# [関数呼び出し]読み込んだ画像のサイズを編集
img_edit.img_edit(img)

sys.exit()

hight,width = img.shape[:2]

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