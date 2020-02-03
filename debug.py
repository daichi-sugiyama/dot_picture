from pylsd.lsd import lsd
import cv2
import numpy as np

# 画像をリサイズして各パラメータを取得
def getImageElement(src_in = 'input.jpg'): #入力画像のパス
    src_out = 'output.jpg' #出力画像のパス

    img = cv2.imread(src_in)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    linesL = lsd(gray)
    # 画像をトリミング
    x = list();
    y = list();
    for line in linesL:
        x1, y1, x2, y2 = map(int,line[:4])
        x.append(x1)
        x.append(x2)
        y.append(y1)
        y.append(y2)
    x_max = max(x)
    x_min = min(x)
    y_max = max(y)
    y_min = min(y)
    img = img[y_min:y_max,x_min:x_max]

    # BGR -> グレースケール
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # エッジ抽出 (Canny) → ２色化して反転することでマス目の線を目立たせる
    ret, threshold_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    edges = cv2.bitwise_not(threshold_img)

    # 膨張処理
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    edges = cv2.dilate(edges, kernel)
    # 輪郭抽出
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 面積でフィルタリング
    rects = []
    for cnt, hrchy in zip(contours, hierarchy[0]):
        if cv2.contourArea(cnt) < 40:
            continue  # 面積が大きいものは除く
        if hrchy[3] == -1:
            continue  # ルートノードは除く
        # 輪郭を囲む長方形を計算する。
        rect = cv2.minAreaRect(cnt)
        rect_points = cv2.boxPoints(rect).astype(int)
        rects.append(rect_points)

    # x-y 順でソート
    rects = sorted(rects, key=lambda x: (x[0][1], x[0][0]))

    diff = list()
    for i, rect in enumerate(rects):
        color = np.random.randint(0, 255, 3).tolist()
        cv2.drawContours(img, rects, i, color, 2)
        # 各正方形の縦と横の値を求める
        x_diff = abs(rect[0][0] - rect[2][0])
        y_diff = abs(rect[0][1] - rect[1][1])
        if(x_diff == y_diff):
            diff.append([x_diff, y_diff])

    cv2.imwrite('output.jpg', img)
    height, width, _ = img.shape[:3]

    # x-yのマス数を求める
    x_count = int(width / (diff[0][0] + 2))
    y_count = int(height / (diff[0][1] + 2))
    print (width, height)
    print (x_count, y_count)
    return x_count, y_count, width, height

getImageElement()