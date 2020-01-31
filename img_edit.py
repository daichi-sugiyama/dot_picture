# 画像を受け取り編集した画像を返す
import cv2

# return:加工した画像のインスタンス, 横のマス目数, 縦のマス目数
def img_edit(img):
	img, crop_im = crop(img)
	## 保存
	cv2.imwrite('img/output.png', crop_im)


# 余白を削除する関数
def crop(img): #引数は画像の相対パス
    # 周りの部分は強制的にトリミング
    h, w = img.shape[:2]
    h1, h2 = int(h * 0.05), int(h * 0.95)
    w1, w2 = int(w * 0.05), int(w * 0.95)
    img = img[h1: h2, w1: w2]
    # cv2.imshow('img', img)

    # Grayscale に変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', gray)

    # 色空間を二値化
    img2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    # cv2.imshow('img2', img2)

    # 輪郭を抽出
    contours = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

    # 輪郭の座標をリストに代入していく
    x1 = [] #x座標の最小値
    y1 = [] #y座標の最小値
    x2 = [] #x座標の最大値
    y2 = [] #y座標の最大値
    for i in range(1, len(contours)):# i = 1 は画像全体の外枠になるのでカウントに入れない
        ret = cv2.boundingRect(contours[i])
        x1.append(ret[0])
        y1.append(ret[1])
        x2.append(ret[0] + ret[2])
        y2.append(ret[1] + ret[3])

    # 輪郭の一番外枠を切り抜き
    x1_min = min(x1)
    y1_min = min(y1)
    x2_max = max(x2)
    y2_max = max(y2)
    cv2.rectangle(img, (x1_min, y1_min), (x2_max, y2_max), (0, 255, 0), 3)

    crop_img = img2[y1_min:y2_max, x1_min:x2_max]
    # cv2.imshow('crop_img', crop_img)

    return img, crop_img