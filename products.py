products = []
count = 0
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入價錢:')
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])
	count += 1
	#total = sum(products.p[1])

print('總共買了', count,'樣東西')
#print('總共花了', total,'元')

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')