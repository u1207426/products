# 二維清單

products = [] #大清單
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ')
	# p = [] # 小清單
	# p.append(name)
	# p.append(price)
	# p = [name, price]
	products.append([name, price])
print(products)
