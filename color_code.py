# RGBの値によって16種類の絵文字を取得
## 絵文字を返す
def make_dot(R, G, B):
	color_code = color_code_conversion(R, G, B)
	if '#000000' == color_code:
		return '⬛'
	elif '#808080' == color_code or '#C0C0C0' == color_code or '#FFFFFF' == color_code:
		return '⬜️'
	elif '#000080' == color_code or '#0080FF' == color_code or '#0000FF'== color_code:
		return '📘'
	elif '#008080' == color_code:
		return '✅'
	elif '#008000' == color_code or '#00FF80' == color_code or '#80FF80' == color_code:
		return '✅'
	elif '#00FF00' == color_code or '#80FF00' == color_code or '#FFFF80' == color_code:
		return '✅'
	elif '#00FFFF' == color_code or '#80FFFF' == color_code:
		return '🚾'
	elif '#FFFF00' == color_code or '#FF8000' == color_code:
		return '🆚'
	elif '#FF0000' == color_code or '#FF0080' == color_code:#'#FF0080'赤っぽいピンク
		return '🆑'
	elif '#FF00FF' == color_code or '#FF8080' == color_code or '#FF80FF' == color_code:
		return '👛'
	elif '#808000' == color_code:
		return '📔'
	elif '#800080' == color_code or '#8000FF' == color_code or '#8080FF' == color_code:
		return '🆔'
	elif '#800000' == color_code:
		return '📕'
	else:
		return (color_code)

## カラーコードを64種類の中で一番近いものに変換する
def color_code_conversion(R, G, B):
	if R < 85:
		R = 0
	elif 85 <=  R <= 169:
		R = 128
	elif 170 <=  R <= 255:
		R = 255
	else:
		print("Rが不正です。")

	if G < 85:
		G = 0
	elif 85 <= G <= 169:
		G = 128
	elif 170 <= G <= 255:
		G = 255
	else:
		print("Gが不正です。")

	if B < 85:
		B = 0
	elif 85 <= B <= 169:
		B = 128
	elif 170 <= B <= 255:
		B = 255
	else:
		print("Bが不正です。")

	color_code = '#%02X%02X%02X' % (R, G, B)

	return color_code