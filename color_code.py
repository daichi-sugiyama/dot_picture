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
		return '⬛'
	elif '#808080' == color_code_conversion(R, G, B):
		return '⬜️'
	elif '#C0C0C0' == color_code_conversion(R, G, B):
		return '⬜️'
	elif '#FFFFFF' == color_code_conversion(R, G, B):
		return '🏳️'
	elif '#0000FF' == color_code_conversion(R, G, B):
		return '📘'
	elif '#000080' == color_code_conversion(R, G, B):
		return '🏧'
	elif '#008080' == color_code_conversion(R, G, B):
		return '🇸🇱'
	elif '#008000' == color_code_conversion(R, G, B):
		return '✅'
	elif '#00FF00' == color_code_conversion(R, G, B):
		return '🥎'
	elif '#00FFFF' == color_code_conversion(R, G, B):
		return '🚾'
	elif '#FFFF00' == color_code_conversion(R, G, B):
		return '🆚'
	elif '#FF0000' == color_code_conversion(R, G, B):
		return '🆑'
	elif '#FF00FF' == color_code_conversion(R, G, B):
		return '👛'
	elif '#808000' == color_code_conversion(R, G, B):
		return '🎞'
	elif '#800080' == color_code_conversion(R, G, B):
		return '🆔'
	elif '#800000' == color_code_conversion(R, G, B):
		return '🗂'
	else:
		print ("カラーコードは不正です")