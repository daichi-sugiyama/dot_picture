import cv2
import numpy as np

# 画像を認識
img = cv2.imread("input.jpg")
img2 = img.copy()
img3 = img.copy()

# グレースケール
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("calendar_mod.png", gray)
# 反転
gray2 = cv2.bitwise_not(gray)
cv2.imwrite("calendar_mod2.png", gray2)
# ラインを取得
lines = cv2.HoughLinesPlines = cv2.HoughLinesP(gray2, rho=1, theta=np.pi/360, threshold=200, minLineLength=200, maxLineGap=5)

count = 0
for line in lines:
    x1, y1, x2, y2 = line[0]

    # 赤線を引く
    red_lines_img = cv2.line(img2, (x1,y1), (x2,y2), (0,0,255), thickness=1)
    cv2.imwrite("calendar_mod3.png", red_lines_img)
    count = count+1
print(count)