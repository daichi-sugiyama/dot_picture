# RGBの値によって16種類の絵文字を取得
## カラーコードを16種類の中で一番近いものに変換する
def color_code_conversion(R, G, B):
    if R < 64:
        R = 0
    elif(64 <=  R <= 160):
        R = 128
    elif(161 <= R <= 223):
        R = 192
    elif(224 <=  R <= 255):
        R = 255
    else:
        print("Rが不正です。")

    if G < 64:
        G = 0
    elif(64 <= G <= 160):
        G = 128
    elif(161 <= G <= 223):
        G = 192
    elif(224 <= G <= 255):
        G = 255
    else:
        print("Gが不正です。")

    if B < 64:
        B = 0
    elif(64 <= B <= 160):
        B = 128
    elif(161 <= B <= 223):
        B = 192
    elif(224 <= B <= 255):
        B = 255
    else:
        print("Bが不正です。")

    color = (R, G, B)
    color_code = '#%02X%02X%02X' % (color[0],color[1],color[2])

    return color_code

## [todo]絵文字を返す
def make_dot(R, G, B):
	if '#000000' == color_code_conversion(R, G, B):
		return '黒'⬛
	elif '#808080' == color_code_conversion(R, G, B):
		return '灰'⬜️
	elif '#C0C0C0' == color_code_conversion(R, G, B):
		return '銀'⬜️
	elif '#FFFFFF' == color_code_conversion(R, G, B):
		return '白'🏳️
	elif '#0000FF' == color_code_conversion(R, G, B):
		return '青'📘
	elif '#000080' == color_code_conversion(R, G, B):
		return '紺'🏧
	elif '#008080' == color_code_conversion(R, G, B):
		return '青緑'🇸🇱
	elif '#008000' == color_code_conversion(R, G, B):
		return '緑'✅
	elif '#00FF00' == color_code_conversion(R, G, B):
		return '来夢'🥎
	elif '#00FFFF' == color_code_conversion(R, G, B):
		return '水色'🚾
	elif '#FFFF00' == color_code_conversion(R, G, B):
		return '黄色'🆚
	elif '#FF0000' == color_code_conversion(R, G, B):
		return '赤'🆑
	elif '#FF00FF' == color_code_conversion(R, G, B):
		return 'ピンク'👛
	elif '#808000' == color_code_conversion(R, G, B):
		return '金'🎞
	elif '#800080' == color_code_conversion(R, G, B):
		return '紫'🆔
	elif '#800000' == color_code_conversion(R, G, B):
		return '茶'🗂
	else:
		print ("カラーコードは不正です")