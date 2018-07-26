file = open('price.txt','r')
print(file.read())
data = []
line = file.readline()
while (line != ''):
	line = line.replace('\n', '')
	row = line.split(',')
	for elem in row:
		index = row.index(elem)
		row[index] = elem.strip()
	data.append(row)
	#print(row)
	line = file.readline()
print(data)

#average price
#option to choose item
#print recipt
