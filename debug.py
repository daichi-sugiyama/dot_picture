from pylsd.lsd import lsd
import cv2

src = 'img/input.jpg' #入力画像のパス
img = cv2.imread(src)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray,(5,5),5) # ガウシアンフィルタを使用した方が良いらしい
linesL = lsd(gray)
for line in linesL:
    x1, y1, x2, y2 = map(int,line[:4])
    lines_img = cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 1)
cv2.imwrite('output.jpg', lines_img)