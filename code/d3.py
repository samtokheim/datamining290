import csv

with open('data.csv', 'rU') as d:
	reader = csv.reader(d)
	data = []
	for row in reader:
		data.append(row[0])
	data_string = ','.join(data[0:200])	
	print data_string		



