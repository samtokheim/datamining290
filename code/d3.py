import csv

with open('1.out', 'rU') as d:
	reader = csv.reader(d)
	data = []
	for row in reader:
		r = row[0].split('\t')
		data.append(r[1])
	data = sorted(data, reverse=True)
	data_string = ','.join(data[0:200])	
	print data_string		



