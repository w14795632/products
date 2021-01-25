products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p.append(name)
	p.append(price)
	##速寫上述三行可簡寫為 p = [name, price]

	products.append(p)

	##更快速簡寫 products.append([name, price])
print(products)


products[0][0]