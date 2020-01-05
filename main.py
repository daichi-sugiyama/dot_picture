# 画像のサイズを変更する
# グリッド線を引く
# 各マス目の色を取得
# colorCodeに変換

import cv2
import numpy as np
import color_code

# 画像を入力
fname = "input.jpg"
img = cv2.imread(fname)

# [todo]画像をドット絵化


# 高さを150,幅を300に変更する
hight = 300
wight = 150
newImg = cv2.resize(img, (hight, wight))

# 保存
cv2.imwrite('output.png',newImg)

# 新しくできた画像を読み込み
img = cv2.imread('output.png')

# 画像の座標によって色を選定
y = 25
x = 25
count = 0
nline = 6 #ドット絵の１行
dot = ''
for i in range (y, wight, 50):
	for j in range (x, hight, 50):
		count += 1
		# GBRを取得
		color = img[i, j]
		# colorCodeを変換
		dot += str(color_code.make_dot(color[2], color[1], color[0]))
		# 改行処理
		if count % nline == 0:
			dot += '\n'

print (dot)