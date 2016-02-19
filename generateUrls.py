f = open('Urls.txt','w')

for i in range(707000, 0, -1):
	page = str(i);
	if i < 10:
		f.write('http://www.books.com.tw/products/001000000' + page)
		f.write('\n')
	elif i < 100 and i >= 10:
		f.write('http://www.books.com.tw/products/00100000' + page)
		f.write('\n')
	elif i < 1000 and i >= 100:
		f.write('http://www.books.com.tw/products/0010000' + page)
		f.write('\n')
	elif i < 10000 and i >= 1000:
		f.write('http://www.books.com.tw/products/001000' + page)
		f.write('\n')
	elif i < 100000 and i >= 10000:
		f.write('http://www.books.com.tw/products/00100' + page)
		f.write('\n')
	elif i < 1000000 and i >= 100000:
		f.write('http://www.books.com.tw/products/0010' + page)
		f.write('\n')

f.close()


