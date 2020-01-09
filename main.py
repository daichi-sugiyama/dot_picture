import cv2
import numpy as np
import color_code

# 画像を入力
fname = "input.jpg"
img = cv2.imread(fname)

# [todo]画像のサイズをなんとかする
## 画像の高さと幅を取得
h,w = img.shape[:2]

# 高さを600,幅を400に変更する
hight = 600
width = 400
newImg = cv2.resize(img, (width, hight))

# 保存
cv2.imwrite('output.png',newImg)

# 新しくできた画像を読み込み
img = cv2.imread('output.png')

# 画像の座標によって色を選定
## １マス25×25
## ヨコ 16 タテ 24
y = 12 #12.5
x = 12 #12.5
count = 0
nline = 16 # ドット絵の１行
dot = ''
for i in range (y, hight, 25):
	for j in range (x, width, 25):
		count += 1
		# GBRを取得
		color = img[i, j]
		# colorCodeを変換
		dot += str(color_code.make_dot(color[2], color[1], color[0]))
		# 改行処理
		if count % nline == 0:
			dot += '\n'

print (dot)