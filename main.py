import cv2
import sys
import numpy as np
import color_code
import get_image_element

# 入力する画像
input_image_path = "input.jpg"

# 各パラメータを取得
x_count, y_count, x_step, y_step, img = get_image_element.get_image_element(input_image_path)

print (x_count, y_count, x_step, y_step)
# 加工した画像の座標の色によって絵文字を選定
x = int(x_step / 2)
y = int(y_step / 2)
nline = x_count # ドット絵の１行:ヨコ

dot = ''
count = 0
for i in range (y, y_step * y_count, y_step):
	for j in range (x, x_step * x_count, x_step):
		count += 1
		# GBRを取得
		color = img[i, j]
		# colorCodeを変換
		dot += str(color_code.make_dot(color[2], color[1], color[0]))
		# 改行処理
		if count % nline == 0:
			dot += '\n'

print (dot)