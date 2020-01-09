color = [0, 128, 255]

# 既存のリスト
list = ['#000000','#808080','#C0C0C0','#FFFFFF','#0000FF','#000080','#008080','#008000','#00FF00','#00FFFF','#FFFF00','#FF0000','#FF00FF','#808000','#800080','#800000']

for i in color:
	for j in color:
		for k in color:
			color_code = '#%02X%02X%02X' % (i, j, k)
			if not color_code in list:
				print (color_code)